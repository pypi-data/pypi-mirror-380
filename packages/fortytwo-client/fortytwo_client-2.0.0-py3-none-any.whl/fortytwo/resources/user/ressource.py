"""
This module provides ressources for getting project users from the 42 API.
"""

from typing import Any, List, Self

from fortytwo.resources.ressource import FortyTwoRessource, RessourceTemplate
from fortytwo.resources.user.user import FortyTwoUser


class GetUsers(FortyTwoRessource[List[FortyTwoUser]]):
    """
    This class provides a ressource for getting all users.
    """

    method: str = "GET"
    _url: str = "/users"

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return [FortyTwoUser(user) for user in response_data]


class GetUserById(FortyTwoRessource[FortyTwoUser]):
    """
    This class provides a ressource for getting a user by its id.
    """

    method: str = "GET"
    _url: str = "/users/%s"

    def __init__(self: Self, user_id: int) -> None:
        self.user_id = user_id

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url % self.user_id

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return FortyTwoUser(response_data)
