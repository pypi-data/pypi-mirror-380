"""Azure Service Bus Queue Adapter."""

import json
from typing import Dict, Any, Callable, Awaitable
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

from ..queue_interface import QueueInterface


class AzureServiceBusAdapter(QueueInterface):
    """Azure Service Bus implementation of QueueInterface."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize Azure Service Bus adapter.
        
        Args:
            config: Configuration dictionary with connection string
        """
        self.config = config
        self.connection_string = config.get('connection_string')
        if not self.connection_string:
            raise ValueError("connection_string is required for Azure Service Bus")
        
        self.client = None
        self.receivers = {}
        self.connected = False

    async def connect(self) -> None:
        """Connect to Azure Service Bus."""
        try:
            self.client = ServiceBusClient.from_connection_string(
                self.connection_string
            )
            self.connected = True
            print("✓ Connected to Azure Service Bus")
        except Exception as e:
            print(f"Failed to connect to Azure Service Bus: {e}")
            raise

    async def disconnect(self) -> None:
        """Disconnect from Azure Service Bus."""
        try:
            # Close all receivers
            for queue_name, receiver in self.receivers.items():
                await receiver.close()
                print(f"✓ Closed receiver for queue: {queue_name}")
            
            self.receivers.clear()

            if self.client:
                await self.client.close()
            
            self.connected = False
            print("✓ Disconnected from Azure Service Bus")
        except Exception as e:
            print(f"Error disconnecting from Azure Service Bus: {e}")
            raise

    async def publish(self, queue_name: str, message: Dict[str, Any], options: Dict[str, Any] = None) -> None:
        """Publish a message to Azure Service Bus queue."""
        if not self.client:
            raise Exception("Not connected to Azure Service Bus")

        options = options or {}

        try:
            async with self.client:
                sender = self.client.get_queue_sender(queue_name=queue_name)
                async with sender:
                    msg = ServiceBusMessage(
                        json.dumps(message),
                        content_type='application/json'
                    )
                    await sender.send_messages(msg)

            print(f"✓ Published message to Azure Service Bus queue: {queue_name}")
        except Exception as e:
            print(f"Error publishing to Azure Service Bus: {e}")
            raise

    async def subscribe(
        self,
        queue_name: str,
        handler: Callable[[Dict[str, Any]], Awaitable[None]],
        options: Dict[str, Any] = None
    ) -> None:
        """Subscribe to Azure Service Bus queue and process messages."""
        if not self.client:
            raise Exception("Not connected to Azure Service Bus")

        options = options or {}

        try:
            receiver = self.client.get_queue_receiver(queue_name=queue_name)
            self.receivers[queue_name] = receiver

            print(f"✓ Subscribed to Azure Service Bus queue: {queue_name}")

            async with receiver:
                async for msg in receiver:
                    try:
                        content = json.loads(str(msg))
                        await handler(content)
                        
                        # Complete the message
                        await receiver.complete_message(msg)
                    except Exception as e:
                        print(f"Error processing message: {e}")
                        
                        # Abandon the message
                        try:
                            await receiver.abandon_message(msg)
                        except Exception as abandon_error:
                            print(f"Error abandoning message: {abandon_error}")

        except Exception as e:
            print(f"Error subscribing to Azure Service Bus: {e}")
            raise

    def is_connected(self) -> bool:
        """Check if connected to Azure Service Bus."""
        return self.connected

