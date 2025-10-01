from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from fortytwo.resources.user.ressource import GetUserById, GetUsers

if TYPE_CHECKING:
    from fortytwo.client import FortyTwoClient
    from fortytwo.request.parameter.parameter import FortyTwoParam
    from fortytwo.resources.user.user import FortyTwoUser


class UserManager:
    """
    Manager for user-related API operations.
    """

    def __init__(self, client: FortyTwoClient) -> None:
        self._client = client

    def get_by_id(self, user_id: int, *params: FortyTwoParam) -> Optional[FortyTwoUser]:
        """
        Get a user by ID.

        Args:
            user_id: The user ID to fetch
            *params: Additional request parameters

        Returns:
            FortyTwoUser object or None if request failed
        """
        return self._client.request(GetUserById(user_id), *params)

    def get_all(self, *params: FortyTwoParam) -> Optional[List[FortyTwoUser]]:
        """
        Get all users.

        Args:
            *params: Additional request parameters

        Returns:
            List of FortyTwoUser objects or None if request failed
        """
        return self._client.request(GetUsers(), *params)
