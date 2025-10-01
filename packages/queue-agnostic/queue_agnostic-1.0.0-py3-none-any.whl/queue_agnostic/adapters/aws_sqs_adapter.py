"""AWS SQS Queue Adapter."""

import json
import asyncio
from typing import Dict, Any, Callable, Awaitable
import aioboto3

from ..queue_interface import QueueInterface


class AWSSQSAdapter(QueueInterface):
    """AWS SQS implementation of QueueInterface."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize AWS SQS adapter.
        
        Args:
            config: Configuration dictionary with AWS credentials
        """
        self.config = config
        self.region = config.get('region', 'us-east-1')
        self.session = None
        self.client = None
        self.queue_urls = {}
        self.polling_tasks = {}
        self.connected = False

    async def connect(self) -> None:
        """Connect to AWS SQS."""
        try:
            self.session = aioboto3.Session(
                aws_access_key_id=self.config.get('aws_access_key_id'),
                aws_secret_access_key=self.config.get('aws_secret_access_key'),
                region_name=self.region
            )
            self.connected = True
            print("✓ Connected to AWS SQS")
        except Exception as e:
            print(f"Failed to connect to AWS SQS: {e}")
            raise

    async def disconnect(self) -> None:
        """Disconnect from AWS SQS."""
        try:
            # Stop all polling tasks
            for queue_name, task in self.polling_tasks.items():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
                print(f"✓ Stopped polling queue: {queue_name}")
            
            self.polling_tasks.clear()
            self.connected = False
            print("✓ Disconnected from AWS SQS")
        except Exception as e:
            print(f"Error disconnecting from AWS SQS: {e}")
            raise

    async def _get_queue_url(self, queue_name: str) -> str:
        """Get the URL for a queue."""
        if queue_name in self.queue_urls:
            return self.queue_urls[queue_name]

        async with self.session.client('sqs', region_name=self.region) as sqs:
            response = await sqs.get_queue_url(QueueName=queue_name)
            url = response['QueueUrl']
            self.queue_urls[queue_name] = url
            return url

    async def publish(self, queue_name: str, message: Dict[str, Any], options: Dict[str, Any] = None) -> None:
        """Publish a message to AWS SQS queue."""
        if not self.connected:
            raise Exception("Not connected to AWS SQS")

        options = options or {}

        try:
            queue_url = await self._get_queue_url(queue_name)
            
            async with self.session.client('sqs', region_name=self.region) as sqs:
                await sqs.send_message(
                    QueueUrl=queue_url,
                    MessageBody=json.dumps(message),
                    DelaySeconds=options.get('delay_seconds', 0)
                )

            print(f"✓ Published message to AWS SQS queue: {queue_name}")
        except Exception as e:
            print(f"Error publishing to AWS SQS: {e}")
            raise

    async def subscribe(
        self,
        queue_name: str,
        handler: Callable[[Dict[str, Any]], Awaitable[None]],
        options: Dict[str, Any] = None
    ) -> None:
        """Subscribe to AWS SQS queue and process messages."""
        if not self.connected:
            raise Exception("Not connected to AWS SQS")

        options = options or {}

        try:
            queue_url = await self._get_queue_url(queue_name)
            polling_interval = options.get('polling_interval', 1)
            max_messages = options.get('max_messages', 1)
            wait_time = options.get('wait_time_seconds', 20)
            visibility_timeout = options.get('visibility_timeout', 30)

            print(f"✓ Subscribed to AWS SQS queue: {queue_name}")

            async def poll_messages():
                async with self.session.client('sqs', region_name=self.region) as sqs:
                    while True:
                        try:
                            response = await sqs.receive_message(
                                QueueUrl=queue_url,
                                MaxNumberOfMessages=max_messages,
                                WaitTimeSeconds=wait_time,
                                VisibilityTimeout=visibility_timeout
                            )

                            messages = response.get('Messages', [])
                            for msg in messages:
                                try:
                                    content = json.loads(msg['Body'])
                                    await handler(content)
                                    
                                    # Delete message after successful processing
                                    await sqs.delete_message(
                                        QueueUrl=queue_url,
                                        ReceiptHandle=msg['ReceiptHandle']
                                    )
                                except Exception as e:
                                    print(f"Error processing message: {e}")
                                    # Message will become visible again after timeout

                            await asyncio.sleep(polling_interval)
                        except asyncio.CancelledError:
                            break
                        except Exception as e:
                            print(f"Error polling messages: {e}")
                            await asyncio.sleep(polling_interval)

            # Start polling task
            task = asyncio.create_task(poll_messages())
            self.polling_tasks[queue_name] = task
            await task

        except Exception as e:
            print(f"Error subscribing to AWS SQS: {e}")
            raise

    def is_connected(self) -> bool:
        """Check if connected to AWS SQS."""
        return self.connected

