# AzPaddyPy

Comprehensive Python logger for Azure, integrating OpenTelemetry for advanced, structured, and distributed tracing.

A standardized Python package for Azure cloud services integration with builder patterns, OpenTelemetry tracing, and comprehensive configuration management.

## Module Architecture

```
azpaddypy/
|
+-- mgmt/                     # Management Services
|   +-- logging.py            # OpenTelemetry Azure Logger
|   +-- identity.py           # Azure Identity Management
|   +-- local_env.py          # Local Environment Variables
|   +-- mgmt_config.py        # Management Configuration
|
+-- resources/                # Azure Resource Clients
|   +-- storage.py            # Blob, File, Queue Storage
|   +-- keyvault.py           # Secrets, Keys, Certificates
|   +-- cosmosdb.py           # Cosmos DB Client
|
+-- builder/                  # Builder Pattern Architecture
|   +-- configuration.py     # ConfigurationSetupBuilder
|   +-- mgmt_builder.py       # AzureManagementBuilder
|   +-- resource_builder.py   # AzureResourceBuilder
|   +-- directors.py          # Pre-configured Directors
|
+-- tools/                    # Higher-Level Tools
|   +-- configuration_manager.py  # Multi-source Config
|   +-- cosmos_prompt_manager.py  # Cosmos Prompt Storage
|
+-- errors/                   # Custom Exception Classes
    +-- exceptions.py         # AzPaddyPyError, ConfigError

Configuration Flow:
[.env files] --> [ConfigurationSetupBuilder] --> [Environment Config]
                                                         |
[Management Services] <-- [AzureManagementBuilder] <----+
        |                                               |
        v                                               |
[Resource Services] <-- [AzureResourceBuilder] <--------+
        |
        v
[Application Usage]

Builder Pattern Composition:
ConfigurationSetupDirector.build_default_config()
  --> AzureManagementBuilder(env_config).with_logger().with_identity()
    --> AzureResourceBuilder(mgmt, env_config).with_storage().with_keyvault()
```



## Key Features

- **OpenTelemetry Integration**: Distributed tracing with Azure Monitor
- **Builder Pattern Architecture**: Flexible service composition
- **Comprehensive Azure SDK Integration**: Storage, Key Vault, Cosmos DB, Identity
- **Environment Detection**: Automatic configuration for local/cloud deployment
- **Token Caching**: Secure Azure identity management
- **Configuration Management**: Multi-source environment and JSON configuration

## Installation

```bash
pip install azpaddypy
```

## Quick Start Examples

### Basic Logger Setup

```python
from azpaddypy.mgmt.logging import AzureLogger

# Initialize with Application Insights
logger = AzureLogger(
    service_name="my-app",
    connection_string="InstrumentationKey=your-key;IngestionEndpoint=https://..."
)

# Use structured logging with correlation
logger.info("Processing user request", extra={
    "user_id": "12345",
    "operation": "data_processing"
})

# Function tracing decorator
@logger.trace_function
def process_data(data):
    logger.info("Processing started", extra={"record_count": len(data)})
    return processed_data
```

### Azure Storage Operations

```python
from azpaddypy.resources.storage import AzureStorage

# Create storage client
storage = AzureStorage(
    account_url="https://myaccount.blob.core.windows.net",
    credential=credential,
    logger=logger
)

# Upload blob with automatic content type detection
blob_url = storage.upload_blob_from_path(
    container_name="documents",
    blob_name="report.pdf",
    file_path="/path/to/report.pdf"
)

# Download blob with encoding detection
content = storage.download_blob_as_text(
    container_name="documents",
    blob_name="data.csv"
)

# Generate SAS URL for secure access
sas_url = storage.generate_blob_sas_url(
    container_name="documents",
    blob_name="report.pdf",
    expiry_hours=24
)
```

### Builder Pattern Configuration

```python
from azpaddypy.builder import AzureManagementBuilder, AzureResourceBuilder
from azpaddypy.builder.directors import ConfigurationSetupDirector

# Create environment configuration
env_config = ConfigurationSetupDirector.build_default_config()

# Build management services (logger, identity)
mgmt = (AzureManagementBuilder(env_config)
        .with_logger()
        .with_identity()
        .build())

# Build resource services (storage, keyvault)
resources = (AzureResourceBuilder(mgmt, env_config)
            .with_storage()
            .with_keyvault()
            .build())

# Access configured services
logger = mgmt.logger
storage = resources.storage
keyvault = resources.keyvault
```

### Configuration Management

```python
from azpaddypy.tools.configuration_manager import ConfigurationManager

# Multi-source configuration with tracking
config_manager = ConfigurationManager(
    environment_config=env_config,
    config_files=[
        "/app/config/settings.json",
        "/app/config/secrets.json"
    ]
)

# Get configuration with origin tracking
database_url = config_manager.get("DATABASE_URL")
api_key = config_manager.get("API_KEY", default="default-key")

# View configuration state
config_manager.print_configuration_state()
```

### Advanced Custom Setup

```python
from azpaddypy.builder.configuration import ConfigurationSetupBuilder

# Custom environment configuration
env_config = (ConfigurationSetupBuilder()
              .with_local_env_management()  # Load .env files first
              .with_environment_detection()
              .with_environment_variables({
                  "CUSTOM_API_URL": "https://api.example.com",
                  "FEATURE_FLAGS": "feature1,feature2"
              }, in_docker=True)
              .with_service_configuration()
              .with_logging_configuration()
              .with_identity_configuration()
              .build())

# Use custom configuration with builders
mgmt = (AzureManagementBuilder(env_config)
        .with_logger(log_level="DEBUG")
        .with_identity(enable_token_cache=True)
        .build())
```

### Cosmos DB Prompt Management

```python
from azpaddypy.tools.cosmos_prompt_manager import CosmosPromptManager

# Initialize with Cosmos DB connection
prompt_manager = CosmosPromptManager(
    cosmos_client=cosmos_client,
    database_name="prompts",
    container_name="templates"
)

# Store and retrieve prompt templates
prompt_manager.store_prompt(
    prompt_id="welcome_message",
    template="Welcome {user_name} to {service_name}!",
    variables=["user_name", "service_name"]
)

# Format prompt with variables
message = prompt_manager.format_prompt(
    prompt_id="welcome_message",
    user_name="Alice",
    service_name="MyApp"
)
```

## Environment Variables

### Core Configuration
- `REFLECTION_NAME`: Service name for Application Insights cloud role
- `REFLECTION_KIND`: Service type (app, functionapp)
- `APPLICATIONINSIGHTS_CONNECTION_STRING`: Application Insights connection

### Storage Configuration
- `STORAGE_ACCOUNT_URL`: Azure Storage Account URL
- `STORAGE_ENABLE_BLOB`: Enable blob storage (default: true)
- `STORAGE_ENABLE_FILE`: Enable file storage (default: true)
- `STORAGE_ENABLE_QUEUE`: Enable queue storage (default: true)

### Key Vault Configuration
- `key_vault_uri`: Azure Key Vault URL
- `KEYVAULT_ENABLE_SECRETS`: Enable secrets access (default: true)
- `KEYVAULT_ENABLE_KEYS`: Enable keys access (default: false)
- `KEYVAULT_ENABLE_CERTIFICATES`: Enable certificates access (default: false)

### Identity Configuration
- `IDENTITY_ENABLE_TOKEN_CACHE`: Enable token caching (default: true)
- `IDENTITY_ALLOW_UNENCRYPTED_STORAGE`: Allow unencrypted cache (default: true)

## Local Development

For local development, AzPaddyPy automatically detects the environment and applies appropriate settings:

```python
# Automatic Azurite emulator configuration for local development
LOCAL_DEVELOPMENT_STORAGE_CONFIG = {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "AzureWebJobsDashboard": "UseDevelopmentStorage=true"
}

# Environment detection in ConfigurationSetupBuilder
env_config = ConfigurationSetupDirector.build_default_config()
```

## Testing

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_storage.py

# Run with coverage
uv run pytest --cov=azpaddypy
```

## Requirements

- Python >= 3.11.10, < 3.12
- Azure SDK packages
- OpenTelemetry integration
- Pydantic for data validation

## License

This project is licensed under the MIT License.