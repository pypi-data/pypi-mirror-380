"""RabbitMQ Queue Adapter."""

import json
import asyncio
from typing import Dict, Any, Callable, Awaitable
import aio_pika
from aio_pika import connect_robust, Message

from ..queue_interface import QueueInterface


class RabbitMQAdapter(QueueInterface):
    """RabbitMQ implementation of QueueInterface."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize RabbitMQ adapter.
        
        Args:
            config: Configuration dictionary with 'url' key
        """
        self.config = config
        self.url = config.get('url', 'amqp://localhost')
        self.connection = None
        self.channel = None

    async def connect(self) -> None:
        """Connect to RabbitMQ."""
        try:
            self.connection = await connect_robust(self.url)
            self.channel = await self.connection.channel()
            print("✓ Connected to RabbitMQ")
        except Exception as e:
            print(f"Failed to connect to RabbitMQ: {e}")
            raise

    async def disconnect(self) -> None:
        """Disconnect from RabbitMQ."""
        try:
            if self.channel:
                await self.channel.close()
            if self.connection:
                await self.connection.close()
            print("✓ Disconnected from RabbitMQ")
        except Exception as e:
            print(f"Error disconnecting from RabbitMQ: {e}")
            raise

    async def publish(self, queue_name: str, message: Dict[str, Any], options: Dict[str, Any] = None) -> None:
        """Publish a message to RabbitMQ queue."""
        if not self.channel:
            raise Exception("Not connected to RabbitMQ")

        options = options or {}
        
        try:
            # Declare queue
            queue = await self.channel.declare_queue(
                queue_name,
                durable=options.get('durable', True)
            )

            # Publish message
            message_body = json.dumps(message).encode()
            await self.channel.default_exchange.publish(
                Message(
                    message_body,
                    delivery_mode=aio_pika.DeliveryMode.PERSISTENT if options.get('persistent', True) else aio_pika.DeliveryMode.NOT_PERSISTENT
                ),
                routing_key=queue_name
            )

            print(f"✓ Published message to RabbitMQ queue: {queue_name}")
        except Exception as e:
            print(f"Error publishing to RabbitMQ: {e}")
            raise

    async def subscribe(
        self,
        queue_name: str,
        handler: Callable[[Dict[str, Any]], Awaitable[None]],
        options: Dict[str, Any] = None
    ) -> None:
        """Subscribe to RabbitMQ queue and process messages."""
        if not self.channel:
            raise Exception("Not connected to RabbitMQ")

        options = options or {}

        try:
            # Declare queue
            queue = await self.channel.declare_queue(
                queue_name,
                durable=options.get('durable', True)
            )

            # Set prefetch count
            if options.get('prefetch'):
                await self.channel.set_qos(prefetch_count=options['prefetch'])

            print(f"✓ Subscribed to RabbitMQ queue: {queue_name}")

            # Process messages
            async def on_message(message: aio_pika.IncomingMessage):
                async with message.process(requeue=options.get('requeue', True)):
                    try:
                        content = json.loads(message.body.decode())
                        await handler(content)
                    except Exception as e:
                        print(f"Error processing message: {e}")
                        raise

            await queue.consume(on_message)

            # Keep running
            await asyncio.Future()  # Run forever

        except Exception as e:
            print(f"Error subscribing to RabbitMQ: {e}")
            raise

    def is_connected(self) -> bool:
        """Check if connected to RabbitMQ."""
        return self.connection is not None and not self.connection.is_closed

