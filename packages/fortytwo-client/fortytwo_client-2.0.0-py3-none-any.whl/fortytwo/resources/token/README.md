# Token Resource

The Token resource provides access to OAuth2 token information and validation for the 42 School API.

## Overview

This module allows you to inspect and validate OAuth2 tokens used for authenticating with the 42 API, including token metadata, scopes, expiration, and application information.

## Classes

### `FortyTwoToken`
Represents OAuth2 token information and metadata.

**Properties:**
- `owner` (Optional[int]): Resource owner ID (user ID who authorized the token, None for client credentials)
- `scopes` (List[str]): List of granted permissions/scopes
- `expires` (int): Token expiration time in seconds from now
- `uid` (str): Application UID that owns this token

### Resource Classes

#### `GetToken`
Fetches information about the current access token.
- **Endpoint:** `https://api.intra.42.fr/oauth/token/info`
- **Method:** GET
- **Returns:** `FortyTwoToken`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo_client import FortyTwoClient

client = FortyTwoClient(
    ...
)

# Get current token information
token_info = client.tokens.get_info()
if token_info:
    print(f"Application UID: {token_info.uid}")
    print(f"Expires in: {token_info.expires} seconds")
    print(f"Scopes: {', '.join(token_info.scopes)}")

    if token_info.owner:
        print(f"Authorized by user: {token_info.owner}")
    else:
        print("Client credentials token (no user)")
```

### Using Resources Directly

```python
from fortytwo_client.resources.token.resource import GetToken

# Get token information
token_info = client.request(GetToken())
```

## Data Structure

### Token Info JSON Response
```json
{
  "resource_owner_id": 12345,
  "scopes": ["public", "projects", "profile"],
  "expires_in_seconds": 7200,
  "application": {
    "uid": "your-app-uid-here"
  }
}
```

## Error Handling

Methods return `None` when:
- Token is invalid or expired
- Network connectivity issues
- Authentication server problems
- Malformed token

```python
token_info = client.tokens.get_info()
if token_info is None:
    print("Unable to retrieve token information")
    print("Possible causes:")
    print("- Token expired")
    print("- Network issues")
    print("- Invalid credentials")
```
