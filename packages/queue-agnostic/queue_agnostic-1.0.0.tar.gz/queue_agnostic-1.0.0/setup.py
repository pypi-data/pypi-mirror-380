"""Setup configuration for queue-agnostic-python package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="queue-agnostic",
    version="1.0.0",
    author="OneZippy",
    author_email="",
    description="Universal queue abstraction library supporting RabbitMQ, AWS SQS, Azure Service Bus, and GCP Pub/Sub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onezippy/queue-agnostic-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "aio-pika>=9.0.0",  # RabbitMQ
        "aioboto3>=11.0.0",  # AWS SQS
        "azure-servicebus>=7.11.0",  # Azure Service Bus
        "google-cloud-pubsub>=2.18.0",  # GCP Pub/Sub
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "python-dotenv>=1.0.0",
        ],
    },
)

