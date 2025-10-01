"""
Queue-Agnostic Python Library

Universal queue abstraction supporting RabbitMQ, AWS SQS, Azure Service Bus, and GCP Pub/Sub.
"""

from .queue_interface import QueueInterface
from .queue_factory import QueueFactory
from .adapters.rabbitmq_adapter import RabbitMQAdapter
from .adapters.aws_sqs_adapter import AWSSQSAdapter
from .adapters.azure_servicebus_adapter import AzureServiceBusAdapter
from .adapters.gcp_pubsub_adapter import GCPPubSubAdapter

__version__ = "1.0.0"
__all__ = [
    "QueueInterface",
    "QueueFactory",
    "RabbitMQAdapter",
    "AWSSQSAdapter",
    "AzureServiceBusAdapter",
    "GCPPubSubAdapter",
]

