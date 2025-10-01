# 42 Client Resources

This directory contains all the resource modules for interacting with the 42 School API. Each resource provides both low-level API access and high-level manager interfaces.

## 📁 Resource Directory Structure

```
resources/
├── user/           # User profiles and authentication
├── project/        # Curriculum projects and metadata
├── project_user/   # Project completion and grading data
├── location/       # Campus workstation and session tracking
├── token/          # OAuth2 token information and validation
└── custom.py       # Custom resource implementations
```

## 🚀 Quick Start

### Using Managers (Recommended)
The easiest way to interact with resources is through the client managers:

```python
from fortytwo_client import FortyTwoClient

client = FortyTwoClient(
    ...
)

# User operations
user = client.users.get(user_id=12345)
users = client.users.get_all()

# Project operations
project = client.projects.get(project_id=1)
projects = client.projects.get_all()

# Location tracking
locations = client.locations.get_by_user(user_id=12345)

# Project completions
completions = client.project_users.get_by_user(user_id=12345)

# Token validation
token_info = client.tokens.get_info()
```

### Using Resources Directly
For fine-grained control, use resource classes directly:

```python
from fortytwo_client.resources.user.ressource import GetUserById
from fortytwo_client.resources.project.resource import GetProjects

# Direct resource usage
user = client.request(GetUserById(12345))
projects = client.request(GetProjects())
```

## 📚 Resource Documentation

Each resource directory contains detailed documentation:

* [User Resource](user/README.md)
* [Project Resource](project/README.md)
* [Project User Resource](project_user/README.md)
* [Location Resource](location/README.md)
* [Token Resource](token/README.md)

## 🔧 Common Patterns

### Error Handling
All resource methods return `None` on errors:

```python
user = client.users.get(user_id=12345)
if user is None:
    print("User not found or request failed")
else:
    print(f"Found user: {user.login}")
```

### Data Serialization
All resource objects support JSON serialization:

```python
import json
from fortytwo_client.json import default_serializer

user = client.users.get(user_id=12345)
user_json = json.dumps(user, default=default_serializer, indent=2)
```

## 🏗️ Architecture Overview

### Resource Classes
Low-level classes that map directly to API endpoints:
- Handle HTTP requests and responses
- Parse JSON data into Python objects
- Provide type-safe interfaces

### Manager Classes
High-level interfaces for common operations:
- Convenient method names (`get`, `get_all`, etc.)
- Parameter validation and defaults
- Consistent error handling

### Data Models
Python classes representing API entities:
- Type-safe property access
- Automatic JSON serialization
- Datetime parsing and formatting

## 🤝 Contributing

When adding new resources:

1. Create a new directory under `resources/`
2. Implement the data model class
3. Create resource classes for API endpoints
4. Add a manager class for convenience methods

## 📖 API Reference

For complete API documentation, see:
- [42 API Documentation](https://api.intra.42.fr/apidoc)
- Individual resource README files in each directory
- Inline code documentation and type hints
