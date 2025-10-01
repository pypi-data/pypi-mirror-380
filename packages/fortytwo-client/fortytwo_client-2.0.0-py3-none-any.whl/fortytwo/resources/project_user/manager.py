from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from fortytwo.resources.project_user.resource import (
    GetProjectUsers,
    GetProjectUsersByProject,
)

if TYPE_CHECKING:
    from fortytwo.client import FortyTwoClient
    from fortytwo.request.params import FortyTwoParam
    from fortytwo.resources.project_user.project_user import FortyTwoProjectUser


class ProjectUserManager:
    """
    Manager for project user-related API operations.
    """

    def __init__(self, client: FortyTwoClient) -> None:
        self._client = client

    def get_all(self, *params: FortyTwoParam) -> Optional[List[FortyTwoProjectUser]]:
        """
        Get all project users.

        Args:
            *params: Additional request parameters

        Returns:
            List of FortyTwoProjectUser objects or None if request failed
        """
        return self._client.request(GetProjectUsers(), *params)

    def get_by_project_id(
        self, project_id: int, *params: FortyTwoParam
    ) -> Optional[List[FortyTwoProjectUser]]:
        """
        Get all project users for a specific project ID.

        Args:
            project_id: The project ID to fetch project users for
            *params: Additional request parameters

        Returns:
            List of FortyTwoProjectUser objects or None if request failed
        """
        return self._client.request(GetProjectUsersByProject(project_id), *params)
