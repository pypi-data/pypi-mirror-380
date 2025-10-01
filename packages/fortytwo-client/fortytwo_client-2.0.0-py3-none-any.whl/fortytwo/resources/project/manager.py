from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from fortytwo.resources.project.resource import (
    GetProjects,
    GetProjectsByCursus,
    GetProjectsById,
)

if TYPE_CHECKING:
    from fortytwo.client import FortyTwoClient
    from fortytwo.request.params import FortyTwoParam
    from fortytwo.resources.project.project import FortyTwoProject


class ProjectManager:
    """
    Manager for project-related API operations.
    """

    def __init__(self, client: FortyTwoClient) -> None:
        self._client = client

    def get_all(self, *params: FortyTwoParam) -> Optional[List[FortyTwoProject]]:
        """
        Get all projects.

        Args:
            *params: Additional request parameters

        Returns:
            List of FortyTwoProject objects or None if request failed
        """
        return self._client.request(GetProjects(), *params)

    def get_by_cursus_id(
        self, cursus_id: int, *params: FortyTwoParam
    ) -> Optional[List[FortyTwoProject]]:
        """
        Get all projects for a specific cursus ID.

        Args:
            cursus_id: The cursus ID to fetch projects for
            *params: Additional request parameters
        Returns:
            List of FortyTwoProject objects or None if request failed
        """

        return self._client.request(GetProjectsByCursus(cursus_id), *params)

    def get_by_id(
        self, project_id: int, *params: FortyTwoParam
    ) -> Optional[FortyTwoProject]:
        """
        Get a project by ID.

        Args:
            project_id: The project ID to fetch
            *params: Additional request parameters

        Returns:
            FortyTwoProject object or None if request failed
        """
        return self._client.request(GetProjectsById(project_id), *params)
