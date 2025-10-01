# Project User Resource

The Project User resource provides access to project completion data, tracking user progress, grades, and team information for 42 School projects.

## Overview

This module allows you to fetch project completion information from the 42 API, including grades, status, team details, and project progression data.

## Classes

### `FortyTwoProjectUser`
Represents a user's completion record for a specific project.

**Properties:**
- `id` (int): Team ID for this project completion
- `name` (str): Team name
- `status` (str): Completion status ("finished", "in_progress", "waiting_for_correction", etc.)
- `final_mark` (int): Final grade received (0-100+)
- `created_at` (datetime): When the project was started
- `updated_at` (datetime): Last update to the project status

### Resource Classes

#### `GetProjectUsers`
Fetches project completion records with filtering options.
- **Endpoint:** `/projects_users`
- **Method:** GET
- **Returns:** `List[FortyTwoProjectUser]`

#### `GetProjectUsersByUserId`
Fetches project completions for a specific user.
- **Endpoint:** `/users/{user_id}/projects_users`
- **Method:** GET
- **Returns:** `List[FortyTwoProjectUser]`

#### `GetProjectUsersByProjectId`
Fetches all completions for a specific project.
- **Endpoint:** `/projects/{project_id}/projects_users`
- **Method:** GET
- **Returns:** `List[FortyTwoProjectUser]`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo_client import FortyTwoClient, params

client = FortyTwoClient(
    ...
)

# Get all project completions for a user
user_projects = client.project_users.get_by_user(user_id=12345)
if user_projects:
    print(f"User completed {len(user_projects)} projects")

    # Show grades
    for project in user_projects:
        status_emoji = "✅" if project.status == "finished" else "🔄"
        print(f"{status_emoji} {project.name}: {project.final_mark}/100")

# Get all completions for a specific project
project_completions = client.project_users.get_by_project(project_id=1)
if project_completions:
    avg_grade = sum(p.final_mark for p in project_completions) / len(project_completions)
    print(f"Average grade for this project: {avg_grade:.1f}/100")
```

### Using Resources Directly

```python
from fortytwo_client.resources.project_user.resource import (
    GetProjectUsers,
    GetProjectUsersByUserId,
    GetProjectUsersByProjectId
)

# Get all project users
all_completions = client.request(GetProjectUsers())

# Get user's project completions
user_completions = client.request(GetProjectUsersByUserId(12345))

# Get project completion statistics
project_stats = client.request(GetProjectUsersByProjectId(1))
```

## Data Structure

### Project User JSON Response
```json
{
  "id": 456789,
  "name": "team_name",
  "status": "finished",
  "final_mark": 95,
  "created_at": "2024-01-15T10:00:00Z",
  "updated_at": "2024-01-22T16:30:00Z"
}
```

## Error Handling

Methods return `None` when:
- No project completion data found
- Authentication fails (401)
- Rate limits are exceeded (429)
- Network errors occur

```python
projects = client.project_users.get_by_user(user_id=99999)
if projects is None:
    print("No project data found or request failed")
elif len(projects) == 0:
    print("User has no project completions")
```
