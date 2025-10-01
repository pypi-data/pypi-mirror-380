"""
This module provides ressources for getting project users from the 42 API.
"""

from typing import Any, List, Self

from fortytwo.resources.project_user.project_user import FortyTwoProjectUser
from fortytwo.resources.ressource import FortyTwoRessource, RessourceTemplate


class GetProjectUsers(FortyTwoRessource[List[FortyTwoProjectUser]]):
    """
    This class provides a ressource for getting all project users.
    """

    method: str = "GET"
    _url: str = "/projects_users"

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return [
            FortyTwoProjectUser(project_user)
            for project_user in response_data
            if project_user["teams"]
        ]


class GetProjectUsersByProject(FortyTwoRessource[List[FortyTwoProjectUser]]):
    """
    This class provides a ressource for getting project users by its project.
    """

    method: str = "GET"
    _url: str = "/projects/%s/projects_users"

    def __init__(self: Self, project_id: int) -> None:
        self.project_id = project_id

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url % self.project_id

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return [
            FortyTwoProjectUser(project_user)
            for project_user in response_data
            if project_user["teams"]
        ]
