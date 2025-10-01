# 42 Client

A Python client library for the 42 School API that simplifies authentication and data retrieval.

## Features

- Easy authentication with 42 API
- Convenient methods for fetching users, projects, locations, and more
- Built-in request handling and error management
- Type hints support
- Customizable request parameters

## Installation

### From PyPI (recommended)

```bash
# Using pip
pip install fortytwo-client

# Using uv (recommended)
uv add fortytwo-client
```

### From source

```bash
git clone https://github.com/lucas-ht/fortytwo-client.git
cd fortytwo-client
uv sync
```

### Development installation

```bash
git clone https://github.com/lucas-ht/fortytwo-client.git
cd fortytwo-client
uv sync --group dev
```

## Quick Start

### 1. Get your API credentials

First, you need to create an application on the [42 API](https://api.intra.42.fr/apidoc) to get your client ID and secret.

### 2. Basic usage

```python
from fortytwo import FortyTwoClient, FortyTwoConfig

# Configure the client
config = FortyTwoConfig(
    ...
)

# Create client instance
client = FortyTwoClient(config)

# Fetch user information
user = client.users.get_by_id(user_id=12345)
print(f"User: {user['login']}")
```

### 3. Advanced usage with custom parameters

```python
from fortytwo import parameter

...

# Use custom parameters for filtering and pagination
user = client.users.get_all(
    # Use the filter by login parameter to fetch user by login
    parameter.UserParameters.Filter.by_login("example")
)
```

### Authentication

The client handles OAuth2 authentication automatically. Simply provide your client credentials in the configuration.

## Examples

See the `example/` directory for more detailed usage examples:

- [`fetch_user.py`](example/fetch_user.py) - Fetching user information
- [`fetch_projects.py`](example/fetch_projects.py) - Working with projects
- [`fetch_location.py`](example/fetch_location.py) - Location data retrieval

## Documentation

For detailed documentation on each resource type:

- [Resources Overview](fortytwo/resources/README.md) - General resource documentation

## License

MIT License - see the LICENSE file for details.

## Links

- [42 API Documentation](https://api.intra.42.fr/apidoc)
- [GitHub Repository](https://github.com/lucas-ht/fortytwo-client)
- [Issue Tracker](https://github.com/lucas-ht/fortytwo-client/issues)
