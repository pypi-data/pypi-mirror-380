# Project Resource

The Project resource provides access to 42 School project data and curriculum information.

## Overview

This module allows you to fetch project information from the 42 API, including project details, difficulty levels, relationships, and curriculum structure.

## Classes

### `FortyTwoProject`
Represents a 42 School project with all associated metadata.

**Properties:**
- `id` (int): Unique project identifier
- `name` (str): Project name
- `slug` (str): URL-friendly project identifier
- `difficulty` (int): Project difficulty level (1-5)
- `exam` (bool): Whether this project is an exam
- `parent` (Optional[Any]): Parent project in curriculum tree
- `children` (List[Any]): Child projects in curriculum tree
- `created_at` (datetime): Project creation date
- `updated_at` (datetime): Last project update date

### Resource Classes

#### `GetProjectsById`
Fetches a single project by its ID.
- **Endpoint:** `/projects/{id}`
- **Method:** GET
- **Returns:** `FortyTwoProject`

#### `GetProjects`
Fetches all projects with optional filtering.
- **Endpoint:** `/projects`
- **Method:** GET
- **Returns:** `List[FortyTwoProject]`

#### `GetProjectsByCursus`
Fetches projects for a specific cursus.
- **Endpoint:** `/cursus/{cursus_id}/projects`
- **Method:** GET
- **Returns:** `List[FortyTwoProject]`

## Usage Examples

### Using the Manager (Recommended)

```python
from fortytwo_client import FortyTwoClient, params

client = FortyTwoClient(
    ...
)

# Get a specific project
project = client.projects.get(project_id=1)
if project:
    print(f"Project: {project.name}")
    print(f"Difficulty: {project.difficulty}/5")
    print(f"Is Exam: {project.exam}")

# Get all projects
projects = client.projects.get_all(
    params.page_size(50),
    params.sort("difficulty")
)
```

### Using Resources Directly

```python
from fortytwo_client.resources.project.resource import (
    GetProjectsById,
    GetProjects,
    GetProjectsByCursus
)

# Get a specific project
project = client.request(GetProjectsById(1))

# Get all projects
projects = client.request(GetProjects())

# Get projects by cursus
cursus_projects = client.request(GetProjectsByCursus(21))
```

## Data Structure

### Project JSON Response
```json
{
  "id": 1,
  "name": "libft",
  "slug": "libft",
  "difficulty": 2,
  "exam": false,
  "parent": {
    "id": 42,
    "name": "42cursus",
    "slug": "42cursus"
  },
  "children": [
    {
      "id": 15,
      "name": "get_next_line",
      "slug": "get_next_line"
    }
  ],
  "created_at": "2019-05-07T08:45:00Z",
  "updated_at": "2024-01-15T12:30:00Z"
}
```

## Error Handling

All methods return `None` when:
- The project is not found (404)
- Authentication fails (401)
- Rate limits are exceeded (429)
- Network errors occur

```python
project = client.projects.get(project_id=99999)
if project is None:
    print("Project not found or request failed")
```
