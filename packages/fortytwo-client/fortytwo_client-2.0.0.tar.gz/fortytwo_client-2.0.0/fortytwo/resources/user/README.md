# User Resource

The User resource provides access to 42 School user data and operations.

## Overview

This module allows you to fetch user information from the 42 API, including basic profile data, authentication status, images, and more.

## Classes

### `FortyTwoUser`
Represents a 42 School user with all their associated data.

**Properties:**
- `id` (int): Unique user identifier
- `login` (str): User's login name
- `kind` (str): User type/kind
- `alumni` (bool): Whether the user is an alumnus
- `active` (bool): Whether the user account is active
- `image` (dict): Profile images in different sizes
- `email` (str): User's email address
- `first_name` (str): User's first name
- `last_name` (str): User's last name
- `usual_full_name` (str): User's display name
- `phone` (str): User's phone number
- `created_at` (datetime): Account creation date
- `updated_at` (datetime): Last profile update date

### Resource Classes

#### `GetUserById`
Fetches a single user by their ID.
- **Endpoint:** `/users/{id}`
- **Method:** GET
- **Returns:** `FortyTwoUser`

#### `GetUsers`
Fetches all users with optional filtering.
- **Endpoint:** `/users`
- **Method:** GET
- **Returns:** `List[FortyTwoUser]`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo_client import FortyTwoClient

client = FortyTwoClient(
    ...
)

# Get a specific user
user = client.users.get(user_id=12345)
if user:
    print(f"User: {user.login}")
    print(f"Name: {user.first_name} {user.last_name}")
    print(f"Alumni: {user.alumni}")
```

### Using Resources Directly

```python
from fortytwo_client.resources.user.ressource import GetUserById, GetUsers

# Get a specific user
user = client.request(GetUserById(12345))

# Get all users
users = client.request(GetUsers())
```

## Data Structure

### User JSON Response
```json
{
  "id": 12345,
  "login": "jdoe",
  "first_name": "John",
  "last_name": "Doe",
  "usual_full_name": "John Doe",
  "email": "john.doe@student.42.fr",
  "kind": "student",
  "alumni?": false,
  "active?": true,
  "phone": "+1234567890",
  "image": {
    "versions": {
      "large": "https://cdn.intra.42.fr/users/large_jdoe.jpg",
      "medium": "https://cdn.intra.42.fr/users/medium_jdoe.jpg",
      "small": "https://cdn.intra.42.fr/users/small_jdoe.jpg",
      "micro": "https://cdn.intra.42.fr/users/micro_jdoe.jpg"
    }
  },
  "created_at": "2023-01-15T10:30:00Z",
  "updated_at": "2024-03-20T14:22:00Z"
}
```

## Error Handling

All methods return `None` when:
- The user is not found (404)
- Authentication fails (401)
- Rate limits are exceeded (429)
- Network errors occur

```python
user = client.users.get(user_id=99999)
if user is None:
    print("User not found or request failed")
```
