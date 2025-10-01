

# Queue-Agnostic Python Library

A flexible, queue-agnostic Python library for processing documents (PDFs, images) that seamlessly works with different queue providers including RabbitMQ, AWS SQS, Azure Service Bus, and Google Cloud Pub/Sub.

## 🚀 Features

- **Provider Agnostic**: Single interface for multiple queue providers
- **Environment-Based Configuration**: Easy deployment across different clients
- **Support for Multiple Providers**:
  - RabbitMQ
  - AWS SQS
  - Azure Service Bus
  - Google Cloud Pub/Sub
- **Async/Await**: Built on asyncio for high performance
- **Automatic Connection Management**: Built-in connection handling
- **Error Handling**: Automatic message retry/requeue on failures
- **Easy to Extend**: Add new queue providers by implementing the QueueInterface

## 📦 Installation

```bash
pip install -e .
```

Or install from requirements:

```bash
pip install -r requirements.txt
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```bash
# Set your queue provider
QUEUE_PROVIDER=rabbitmq  # or aws-sqs, azure-servicebus, gcp-pubsub

# Set your queue/topic name
QUEUE_NAME=document-processing-queue

# For GCP: Topic name for publishing
TOPIC_NAME=document-processing-topic

# Provider-specific configuration (see .env.example for details)
RABBITMQ_URL=amqp://localhost:5672
```

## 📖 Usage

### Quick Start - Subscriber

```python
import asyncio
from dotenv import load_dotenv
from queue_agnostic import QueueFactory

load_dotenv()

async def process_message(message):
    print('Processing:', message)
    # Your document processing logic here

async def main():
    # Create queue from environment variables
    result = QueueFactory.create_from_env()
    queue = result['adapter']
    queue_name = result['queue_name']
    
    await queue.connect()
    
    # Subscribe and process messages
    await queue.subscribe(queue_name, process_message)

asyncio.run(main())
```

### Quick Start - Publisher

```python
import asyncio
from dotenv import load_dotenv
from queue_agnostic import QueueFactory

load_dotenv()

async def main():
    result = QueueFactory.create_from_env()
    queue = result['adapter']
    topic_name = result['topic_name']
    
    await queue.connect()
    
    # Publish a message
    await queue.publish(topic_name, {
        'document_id': 'doc-123',
        'document_url': 'https://example.com/doc.pdf',
        'document_type': 'pdf'
    })
    
    await queue.disconnect()

asyncio.run(main())
```

### Direct Usage (Without Environment Variables)

```python
from queue_agnostic import QueueFactory

# Create queue with explicit configuration
queue = QueueFactory.create({
    'provider': 'rabbitmq',
    'options': {
        'url': 'amqp://localhost:5672'
    }
})

await queue.connect()
# ... use the queue
await queue.disconnect()
```

## 🏗️ Architecture

### Project Structure

```
queue-agnostic-python/
├── queue_agnostic/
│   ├── __init__.py
│   ├── queue_interface.py          # Abstract interface
│   ├── queue_factory.py            # Factory for creating adapters
│   └── adapters/
│       ├── __init__.py
│       ├── rabbitmq_adapter.py     # RabbitMQ implementation
│       ├── aws_sqs_adapter.py      # AWS SQS implementation
│       ├── azure_servicebus_adapter.py  # Azure implementation
│       └── gcp_pubsub_adapter.py   # GCP implementation
├── examples/
│   ├── publisher.py                # Example publisher
│   └── subscriber.py               # Example subscriber
├── setup.py
├── requirements.txt
└── README.md
```

## 🔌 Queue Interface

All adapters implement:

### Methods

- `connect()` - Connect to the queue service
- `disconnect()` - Disconnect from the queue service
- `publish(queue_name, message, options)` - Publish a message
- `subscribe(queue_name, handler, options)` - Subscribe and process messages
- `is_connected()` - Check connection status

## ⚙️ Provider-Specific Configuration

### RabbitMQ

```bash
QUEUE_PROVIDER=rabbitmq
RABBITMQ_URL=amqp://localhost:5672
QUEUE_NAME=my-queue
```

### AWS SQS

```bash
QUEUE_PROVIDER=aws-sqs
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
QUEUE_NAME=my-queue
```

### Azure Service Bus

```bash
QUEUE_PROVIDER=azure-servicebus
AZURE_SERVICEBUS_CONNECTION_STRING=Endpoint=sb://...
QUEUE_NAME=my-queue
```

### Google Cloud Pub/Sub

```bash
QUEUE_PROVIDER=gcp-pubsub
GCP_PROJECT_ID=your-project-id
GCP_KEY_FILENAME=./service-account-key.json
TOPIC_NAME=my-topic              # For publishing
QUEUE_NAME=my-subscription       # For subscribing
```

## 🚀 Running Examples

### Run Subscriber

```bash
python examples/subscriber.py
```

### Run Publisher

```bash
python examples/publisher.py
```

## 🔄 Deployment Scenarios

Same code, different configurations:

**Client A (RabbitMQ)**:
```bash
QUEUE_PROVIDER=rabbitmq
RABBITMQ_URL=amqp://client-a-server:5672
```

**Client B (AWS)**:
```bash
QUEUE_PROVIDER=aws-sqs
AWS_REGION=us-west-2
```

**Client C (Azure)**:
```bash
QUEUE_PROVIDER=azure-servicebus
AZURE_SERVICEBUS_CONNECTION_STRING=Endpoint=sb://...
```

## 🐛 Error Handling

All adapters include built-in error handling:

- **Message Processing Errors**: Messages are automatically requeued/nacked
- **Connection Errors**: Logged and can be handled with reconnection logic
- **Graceful Shutdown**: Proper cleanup on SIGINT/SIGTERM

## 📝 License

MIT

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📞 Support

For issues or questions, please open an issue on the repository.

