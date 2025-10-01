# Location Resource

The Location resource provides access to 42 School location/session data, tracking where and when users work at campus computers.

## Overview

This module allows you to fetch location information from the 42 API, including session data showing when users log in/out of campus computers, their workstation usage patterns, and time tracking.

## Classes

### `FortyTwoLocation`
Represents a location/session record for a user at a campus workstation.

**Properties:**
- `id` (int): Unique location record identifier
- `host` (str): Computer/workstation identifier (e.g., "e1r1p1")
- `begin_at` (datetime): Session start time
- `end_at` (Optional[datetime]): Session end time (None if still active)

### Resource Classes

#### `GetLocationsByUserId`
Fetches location/session history for a specific user.
- **Endpoint:** `/users/{user_id}/locations`
- **Method:** GET
- **Returns:** `List[FortyTwoLocation]`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo_client import FortyTwoClient, params

client = FortyTwoClient(
    ...
)

# Get location history for a user
locations = client.locations.get_by_user(user_id=12345)
if locations:
    print(f"Found {len(locations)} location records")

    # Show current session (if any)
    current_session = next((loc for loc in locations if loc.end_at is None), None)
    if current_session:
        print(f"Currently logged in at: {current_session.host}")
        print(f"Since: {current_session.begin_at}")

    # Show recent sessions
    for location in locations[:5]:
        duration = "ongoing" if location.end_at is None else location.end_at - location.begin_at
        print(f"{location.host}: {location.begin_at} -> {duration}")
```

### Using Resources Directly

```python
from fortytwo_client.resources.location.resource import GetLocationsByUserId

# Get user location history
locations = client.request(GetLocationsByUserId(12345))
```

## Data Structure

### Location JSON Response
```json
{
  "id": 123456,
  "host": "e1r1p1",
  "begin_at": "2024-03-20T09:30:00Z",
  "end_at": "2024-03-20T17:45:00Z"
}
```

### Active Session (end_at is null)
```json
{
  "id": 123457,
  "host": "e2r3p5",
  "begin_at": "2024-03-21T10:15:00Z",
  "end_at": null
}
```

## Error Handling

Methods return `None` when:
- The user is not found (404)
- User has no location data
- Authentication fails (401)
- Rate limits are exceeded (429)
- Network errors occur

```python
locations = client.locations.get_by_user(user_id=99999)
if locations is None:
    print("No location data found or request failed")
elif len(locations) == 0:
    print("User has no location history")
```
