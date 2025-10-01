"""
Abstract Queue Interface

All queue adapters must implement this interface.
"""

from abc import ABC, abstractmethod
from typing import Callable, Dict, Any, Awaitable


class QueueInterface(ABC):
    """Abstract base class for queue adapters."""

    @abstractmethod
    async def connect(self) -> None:
        """
        Connect to the queue service.
        
        Raises:
            Exception: If connection fails
        """
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """
        Disconnect from the queue service.
        
        Raises:
            Exception: If disconnection fails
        """
        pass

    @abstractmethod
    async def publish(self, queue_name: str, message: Dict[str, Any], options: Dict[str, Any] = None) -> None:
        """
        Publish a message to the queue.
        
        Args:
            queue_name: Name of the queue/topic
            message: Message payload (dictionary)
            options: Additional provider-specific options
            
        Raises:
            Exception: If publishing fails
        """
        pass

    @abstractmethod
    async def subscribe(
        self,
        queue_name: str,
        handler: Callable[[Dict[str, Any]], Awaitable[None]],
        options: Dict[str, Any] = None
    ) -> None:
        """
        Subscribe to a queue and process messages.
        
        Args:
            queue_name: Name of the queue/topic
            handler: Async function to handle messages
            options: Additional provider-specific options
            
        Raises:
            Exception: If subscription fails
        """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Check if connection is active.
        
        Returns:
            bool: True if connected, False otherwise
        """
        pass

