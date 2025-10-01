"""Queue Factory for creating queue adapters."""

import os
from typing import Dict, Any, Optional
from .queue_interface import QueueInterface
from .adapters.rabbitmq_adapter import RabbitMQAdapter
from .adapters.aws_sqs_adapter import AWSSQSAdapter
from .adapters.azure_servicebus_adapter import AzureServiceBusAdapter
from .adapters.gcp_pubsub_adapter import GCPPubSubAdapter


class QueueFactory:
    """Factory class for creating queue adapters."""

    @staticmethod
    def create(config: Dict[str, Any]) -> QueueInterface:
        """
        Create a queue adapter based on the provider type.
        
        Args:
            config: Configuration dictionary with 'provider' and 'options' keys
            
        Returns:
            QueueInterface: Queue adapter instance
            
        Raises:
            ValueError: If provider is unsupported
        """
        provider = config.get('provider', '').lower()
        options = config.get('options', {})

        if provider in ('rabbitmq',):
            return RabbitMQAdapter(options)
        elif provider in ('aws-sqs', 'aws', 'sqs'):
            return AWSSQSAdapter(options)
        elif provider in ('azure-servicebus', 'azure', 'servicebus'):
            return AzureServiceBusAdapter(options)
        elif provider in ('gcp-pubsub', 'gcp', 'pubsub', 'google'):
            return GCPPubSubAdapter(options)
        else:
            raise ValueError(
                f"Unsupported queue provider: {provider}. "
                f"Supported providers: rabbitmq, aws-sqs, azure-servicebus, gcp-pubsub"
            )

    @staticmethod
    def create_from_env(overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a queue adapter from environment variables.
        
        Args:
            overrides: Optional dictionary to override environment variables
                - provider: Override QUEUE_PROVIDER
                - queue_name: Override QUEUE_NAME
                - topic_name: Override TOPIC_NAME
                - subscription_name: Override SUBSCRIPTION_NAME
                
        Returns:
            Dictionary with:
                - adapter: QueueInterface instance
                - queue_name: Resolved queue name
                - topic_name: Resolved topic name
                - subscription_name: Resolved subscription name
                
        Raises:
            ValueError: If QUEUE_PROVIDER is not set
        """
        overrides = overrides or {}
        
        provider = overrides.get('provider') or os.getenv('QUEUE_PROVIDER')
        if not provider:
            raise ValueError("QUEUE_PROVIDER environment variable is not set")

        config = {
            'provider': provider,
            'options': {},
            'queue_name': overrides.get('queue_name') or os.getenv('QUEUE_NAME'),
            'topic_name': overrides.get('topic_name') or os.getenv('TOPIC_NAME'),
            'subscription_name': overrides.get('subscription_name') or os.getenv('SUBSCRIPTION_NAME')
        }

        # Load provider-specific configuration
        provider_lower = provider.lower()
        
        if provider_lower == 'rabbitmq':
            config['options'] = {
                'url': os.getenv('RABBITMQ_URL', 'amqp://localhost')
            }
        elif provider_lower in ('aws-sqs', 'aws', 'sqs'):
            config['options'] = {
                'region': os.getenv('AWS_REGION', 'us-east-1'),
                'aws_access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
                'aws_secret_access_key': os.getenv('AWS_SECRET_ACCESS_KEY')
            }
        elif provider_lower in ('azure-servicebus', 'azure', 'servicebus'):
            connection_string = os.getenv('AZURE_SERVICEBUS_CONNECTION_STRING')
            if not connection_string:
                raise ValueError("AZURE_SERVICEBUS_CONNECTION_STRING environment variable is required")
            config['options'] = {
                'connection_string': connection_string
            }
        elif provider_lower in ('gcp-pubsub', 'gcp', 'pubsub', 'google'):
            project_id = os.getenv('GCP_PROJECT_ID')
            if not project_id:
                raise ValueError("GCP_PROJECT_ID environment variable is required")
            config['options'] = {
                'project_id': project_id,
                'credentials_path': os.getenv('GCP_CREDENTIALS_PATH') or os.getenv('GCP_KEY_FILENAME')
            }

        adapter = QueueFactory.create(config)
        
        return {
            'adapter': adapter,
            'queue_name': config['queue_name'],
            'topic_name': config['topic_name'],
            'subscription_name': config['subscription_name']
        }

