# Zero Trust Python SDK

[![PyPI version](https://badge.fury.io/py/zero-trust-sdk.svg)](https://badge.fury.io/py/zero-trust-sdk)
[![Python Support](https://img.shields.io/pypi/pyversions/zero-trust-sdk.svg)](https://pypi.org/project/zero-trust-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful Python SDK for interacting with Zero Trust Blockchain Databases with pandas integration for data scientists and developers.

## 🚀 Features

- **🔐 Complete Authentication** - Email/password and Web3 wallet authentication
- **📊 Pandas Integration** - Seamless DataFrame import/export and querying  
- **🗄️ Database Management** - Create, query, and manage blockchain databases
- **🔄 Data Migration** - Import/export from CSV, JSON, and other databases
- **⚡ Real-time Sync** - Continuous data synchronization from external sources
- **🛡️ Type Safety** - Full type hints and validation
- **🔧 Async/Await** - High-performance async operations
- **📈 Production Ready** - Comprehensive error handling and retry logic

## 📦 Installation

```bash
# Basic installation
pip install zero-trust-sdk

# With async support
pip install zero-trust-sdk[async]

# With data visualization
pip install zero-trust-sdk[visualization]

# With Jupyter notebook support
pip install zero-trust-sdk[jupyter]

# Install everything
pip install zero-trust-sdk[all]

# Development installation
pip install zero-trust-sdk[dev]
```

## 🏃‍♂️ Quick Start

### Basic Usage

```python
import asyncio
from zero_trust import ZeroTrustClient
import pandas as pd

async def main():
    # Create client
    client = await ZeroTrustClient.create("http://localhost:3000")
    
    # Authenticate
    auth_response = await client.auth.login("user@example.com", "password")
    print(f"Logged in as {auth_response.user.email}")
    
    # Create database
    database = await client.databases.create_database("my_app_db")
    print(f"Created database: {database.name}")
    
    # Query data as DataFrame
    df = await client.databases.to_dataframe("my_app_db", "users")
    print(df.head())

# Run async function
asyncio.run(main())
```

### Pandas Integration

```python
import pandas as pd
from zero_trust import ZeroTrustClient

async def pandas_example():
    client = await ZeroTrustClient.create("http://localhost:3000")
    await client.auth.login("user@example.com", "password")
    
    # Create DataFrame
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'London', 'Tokyo']
    })
    
    # Import DataFrame to blockchain database
    migration = await client.migration.import_dataframe(
        database="analytics_db",
        table_name="users", 
        df=df
    )
    print(f"Imported {migration.records_processed} records")
    
    # Query back as DataFrame
    result_df = await client.databases.to_dataframe("analytics_db", "users")
    print(result_df)

asyncio.run(pandas_example())
```

### Data Migration

```python
from zero_trust import ZeroTrustClient

async def migration_example():
    client = await ZeroTrustClient.create("http://localhost:3000")
    await client.auth.login("user@example.com", "password")
    
    # Import from CSV
    with open('data.csv', 'r') as f:
        csv_content = f.read()
    
    await client.migration.import_csv(
        database="imported_data",
        table_name="csv_data",
        csv_content=csv_content,
        has_header=True
    )
    
    # Export to JSON
    json_data = await client.migration.export_to_json(
        database="imported_data",
        table_name="csv_data"
    )
    
    with open('exported_data.json', 'w') as f:
        f.write(json_data)

asyncio.run(migration_example())
```

### Real-time Data Sync

```python
from zero_trust import ZeroTrustClient

async def sync_example():
    client = await ZeroTrustClient.create("http://localhost:3000")
    await client.auth.login("user@example.com", "password")
    
    # Sync data from external API
    result = await client.sync.from_api(
        url="https://jsonplaceholder.typicode.com/users",
        database="external_data",
        table_name="api_users"
    )
    
    print(f"Synced {result.records_synced} records")
    
    # Set up continuous sync
    sync_config = await client.sync.create_sync_config(
        name="api_sync",
        source_type="api",
        source="https://api.example.com/data",
        target="live_data",
        interval=300  # 5 minutes
    )
    
    # Start sync process
    await client.sync.start_sync("api_sync")

asyncio.run(sync_example())
```

## 📖 API Reference

### Client

```python
from zero_trust import ZeroTrustClient, Config

# Create client with custom config
config = Config(
    api_url="https://api.zerotrust.com",
    timeout=60,
    max_retries=5
)
client = ZeroTrustClient(config)

# Or from environment variables
client = await ZeroTrustClient.create_with_defaults()
```

### Authentication

```python
# Email/password authentication
auth_response = await client.auth.register("user@example.com", "password")
auth_response = await client.auth.login("user@example.com", "password")

# Web3 wallet authentication
auth_response = await client.auth.wallet_auth(
    wallet_address="0x...",
    signature="0x...",
    message="Sign this message"
)

# Get current user
user = await client.auth.get_current_user()
```

### Database Operations

```python
# List databases
databases = await client.databases.list_databases()

# Create database
database = await client.databases.create_database("my_db")

# Create table with schema
from zero_trust.types import Column

columns = [
    Column(name="id", data_type="INTEGER", is_primary_key=True),
    Column(name="name", data_type="TEXT", nullable=False),
    Column(name="email", data_type="TEXT"),
]

table = await client.databases.create_table("my_db", "users", columns)

# Insert data
records = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

count = await client.databases.insert_data("my_db", "users", records)

# Query data
result = await client.databases.query_data("my_db", "users", limit=10)
print(result.data.rows)

# Search data
search_result = await client.databases.search_table(
    "my_db", "users", "name", "Alice"
)
```

### SQL Queries

```python
# Execute SQL queries
query_builder = client.databases.query("my_db")

result = await query_builder.execute("SELECT * FROM users WHERE age > 25")
print(result.data.rows)

# Get results as DataFrame
df = await query_builder.to_dataframe("SELECT name, email FROM users")
print(df.head())
```

### Data Migration

```python
# Import from different formats
await client.migration.import_csv(db, table, csv_content)
await client.migration.import_json(db, table, json_content)  
await client.migration.import_dataframe(db, table, df)

# Export to different formats
csv_data = await client.migration.export_to_csv(db, table)
json_data = await client.migration.export_to_json(db, table)
df = await client.migration.export_to_dataframe(db, table)

# Backup and restore
backup = await client.migration.backup_database("my_db")
await client.migration.restore_database(backup, "restored_db")
```

## 🔧 Configuration

### Environment Variables

```bash
export ZEROTRUST_API_URL="http://localhost:3000"
export ZEROTRUST_TOKEN="your_jwt_token"
export ZEROTRUST_TIMEOUT="30"
export ZEROTRUST_MAX_RETRIES="3"
```

### Configuration File

```python
from zero_trust import Config

config = Config(
    api_url="https://api.zerotrust.com",
    token="your_jwt_token", 
    timeout=60,
    max_retries=5,
    verify_ssl=True
)
```

## 🐍 Synchronous Usage

For compatibility with synchronous code:

```python
from zero_trust.http_client import SyncHttpClient
from zero_trust import Config

# Use synchronous client for basic operations
config = Config("http://localhost:3000")
sync_client = SyncHttpClient(config)

# Make synchronous requests
health = sync_client.get("/health")
print(health)
```

## 📊 Jupyter Notebook Integration

```python
# In Jupyter notebook
%pip install zero-trust-sdk[jupyter]

import pandas as pd
from zero_trust import ZeroTrustClient

# Async cells in Jupyter
client = await ZeroTrustClient.create("http://localhost:3000")
await client.auth.login("user@example.com", "password")

# Query and visualize data
df = await client.databases.to_dataframe("analytics", "sales_data")
df.plot(kind='bar', x='month', y='revenue')
```

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src/zero_trust --cov-report=html

# Run specific test
pytest tests/test_client.py::test_authentication

# Run async tests
pytest -v tests/test_async.py
```

## 🛠️ Development

```bash
# Clone repository
git clone https://github.com/your-org/zero-trust-python-sdk.git
cd zero-trust-python-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .[dev]

# Run code formatting
black src/ tests/
isort src/ tests/

# Run type checking
mypy src/

# Run linting
flake8 src/ tests/
```

## 📈 Performance

The SDK is optimized for performance:

- **Async I/O** - Non-blocking operations for high concurrency
- **Connection Pooling** - Reused HTTP connections
- **Batch Operations** - Efficient bulk data operations
- **Streaming** - Memory-efficient large data processing
- **Caching** - Smart caching of metadata and schemas

### Benchmarks

```python
# Benchmark example
import time
import asyncio
from zero_trust import ZeroTrustClient

async def benchmark():
    client = await ZeroTrustClient.create("http://localhost:3000")
    await client.auth.login("user@example.com", "password")
    
    # Benchmark data insertion
    start = time.time()
    
    records = [{"id": i, "value": f"test_{i}"} for i in range(10000)]
    await client.databases.insert_data("benchmark", "test_data", records)
    
    duration = time.time() - start
    print(f"Inserted 10,000 records in {duration:.2f}s ({10000/duration:.0f} records/sec)")

asyncio.run(benchmark())
```

## 🔍 Error Handling

The SDK provides comprehensive error handling:

```python
from zero_trust.types import ZeroTrustError

try:
    await client.databases.create_database("test_db")
except ZeroTrustError as e:
    if e.code == "AUTH_ERROR":
        print("Authentication failed")
    elif e.code == "VALIDATION_ERROR":
        print(f"Validation error: {e.message}")
    elif e.is_retryable:
        print("Temporary error, retrying...")
    else:
        print(f"Error: {e}")
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [https://docs.zerotrust.com/python-sdk](https://docs.zerotrust.com/python-sdk)
- **GitHub Issues**: [https://github.com/your-org/zero-trust-python-sdk/issues](https://github.com/your-org/zero-trust-python-sdk/issues)
- **Discord**: [https://discord.gg/zerotrust](https://discord.gg/zerotrust)
- **Email**: support@zerotrust.com

## 🎯 Roadmap

- [ ] **v0.2.0**: Advanced querying and indexing
- [ ] **v0.3.0**: Real-time subscriptions and webhooks  
- [ ] **v0.4.0**: Multi-chain support (Polygon, BSC, etc.)
- [ ] **v0.5.0**: GraphQL API support
- [ ] **v1.0.0**: Production hardening and performance optimization

---

**Made with ❤️ by the Zero Trust team**

*Secure, scalable, and developer-friendly blockchain database access for Python*