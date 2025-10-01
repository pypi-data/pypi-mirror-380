from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from fortytwo.resources.location.resource import GetLocationsByUserId

if TYPE_CHECKING:
    from fortytwo.client import FortyTwoClient
    from fortytwo.request.params import FortyTwoParam
    from fortytwo.resources.location.location import FortyTwoLocation


class LocationManager:
    """
    Manager for location-related API operations.
    """

    def __init__(self, client: FortyTwoClient) -> None:
        self._client = client

    def get_by_user_id(
        self, user_id: int, *params: FortyTwoParam
    ) -> Optional[List[FortyTwoLocation]]:
        """
        Get locations of a user by user ID.

        Args:
            user_id: The user ID to fetch
            *params: Additional request parameters

        Returns:
            List of FortyTwoLocation object or None if request failed
        """
        return self._client.request(GetLocationsByUserId(user_id), *params)
