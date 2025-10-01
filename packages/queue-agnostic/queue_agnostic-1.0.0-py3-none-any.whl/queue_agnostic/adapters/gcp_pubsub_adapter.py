"""Google Cloud Pub/Sub Queue Adapter."""

import json
import asyncio
from typing import Dict, Any, Callable, Awaitable
from google.cloud import pubsub_v1
from concurrent import futures

from ..queue_interface import QueueInterface


class GCPPubSubAdapter(QueueInterface):
    """Google Cloud Pub/Sub implementation of QueueInterface."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize GCP Pub/Sub adapter.
        
        Args:
            config: Configuration dictionary with project_id and credentials
        """
        self.config = config
        self.project_id = config.get('project_id')
        if not self.project_id:
            raise ValueError("project_id is required for GCP Pub/Sub")
        
        self.credentials_path = config.get('credentials_path')
        self.publisher = None
        self.subscriber = None
        self.subscriptions = {}
        self.connected = False

    async def connect(self) -> None:
        """Connect to GCP Pub/Sub."""
        try:
            if self.credentials_path:
                import os
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credentials_path
            
            self.publisher = pubsub_v1.PublisherClient()
            self.subscriber = pubsub_v1.SubscriberClient()
            self.connected = True
            print("✓ Connected to Google Cloud Pub/Sub")
        except Exception as e:
            print(f"Failed to connect to Google Cloud Pub/Sub: {e}")
            raise

    async def disconnect(self) -> None:
        """Disconnect from GCP Pub/Sub."""
        try:
            # Close all subscriptions
            for subscription_name, future in self.subscriptions.items():
                future.cancel()
                print(f"✓ Closed subscription: {subscription_name}")
            
            self.subscriptions.clear()
            self.connected = False
            print("✓ Disconnected from Google Cloud Pub/Sub")
        except Exception as e:
            print(f"Error disconnecting from Google Cloud Pub/Sub: {e}")
            raise

    async def publish(self, topic_name: str, message: Dict[str, Any], options: Dict[str, Any] = None) -> None:
        """Publish a message to GCP Pub/Sub topic."""
        if not self.publisher:
            raise Exception("Not connected to Google Cloud Pub/Sub")

        options = options or {}

        try:
            topic_path = self.publisher.topic_path(self.project_id, topic_name)
            
            # Create topic if it doesn't exist
            if options.get('create_if_not_exists', True):
                try:
                    self.publisher.create_topic(request={"name": topic_path})
                    print(f"✓ Created topic: {topic_name}")
                except Exception:
                    # Topic already exists
                    pass

            # Publish message
            data = json.dumps(message).encode('utf-8')
            future = self.publisher.publish(topic_path, data)
            message_id = await asyncio.get_event_loop().run_in_executor(None, future.result)

            print(f"✓ Published message to GCP Pub/Sub topic: {topic_name} (Message ID: {message_id})")
        except Exception as e:
            print(f"Error publishing to Google Cloud Pub/Sub: {e}")
            raise

    async def subscribe(
        self,
        subscription_name: str,
        handler: Callable[[Dict[str, Any]], Awaitable[None]],
        options: Dict[str, Any] = None
    ) -> None:
        """Subscribe to GCP Pub/Sub subscription and process messages."""
        if not self.subscriber:
            raise Exception("Not connected to Google Cloud Pub/Sub")

        options = options or {}

        try:
            subscription_path = self.subscriber.subscription_path(
                self.project_id, subscription_name
            )

            # Create subscription if it doesn't exist
            if options.get('create_if_not_exists', True):
                topic_name = options.get('topic_name')
                if not topic_name:
                    raise ValueError("topic_name is required to create a new subscription")
                
                try:
                    topic_path = self.publisher.topic_path(self.project_id, topic_name)
                    self.subscriber.create_subscription(
                        request={"name": subscription_path, "topic": topic_path}
                    )
                    print(f"✓ Created subscription: {subscription_name}")
                except Exception:
                    # Subscription already exists
                    pass

            print(f"✓ Subscribed to GCP Pub/Sub subscription: {subscription_name}")

            def callback(message):
                """Process incoming message."""
                try:
                    content = json.loads(message.data.decode('utf-8'))
                    
                    # Run async handler in event loop
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(handler(content))
                    
                    # Acknowledge the message
                    message.ack()
                except Exception as e:
                    print(f"Error processing message: {e}")
                    # Negative acknowledge (message will be redelivered)
                    message.nack()

            # Subscribe
            streaming_pull_future = self.subscriber.subscribe(
                subscription_path, callback=callback
            )
            self.subscriptions[subscription_name] = streaming_pull_future

            # Keep running
            try:
                await asyncio.get_event_loop().run_in_executor(
                    None, streaming_pull_future.result
                )
            except futures.TimeoutError:
                streaming_pull_future.cancel()

        except Exception as e:
            print(f"Error subscribing to Google Cloud Pub/Sub: {e}")
            raise

    def is_connected(self) -> bool:
        """Check if connected to GCP Pub/Sub."""
        return self.connected

