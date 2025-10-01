"""
This module provides ressources for location of users from the 42 API.
"""

from typing import Any, List, Self

from fortytwo.resources.location.location import FortyTwoLocation
from fortytwo.resources.ressource import FortyTwoRessource, RessourceTemplate


class GetLocationsByUserId(FortyTwoRessource[List[FortyTwoLocation]]):
    """
    This class provides a ressource for getting the locations of a user.
    """

    method: str = "GET"
    _url: str = "/users/%s/locations"

    def __init__(self: Self, user_id: int) -> None:
        self.user_id = user_id

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url % self.user_id

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return [FortyTwoLocation(location) for location in response_data]
