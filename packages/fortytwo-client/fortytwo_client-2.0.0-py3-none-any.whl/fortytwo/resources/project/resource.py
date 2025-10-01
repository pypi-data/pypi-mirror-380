"""
This module provides ressources for getting projects from the 42 API.
"""

from typing import Any, List, Self

from fortytwo.resources.project.project import FortyTwoProject
from fortytwo.resources.ressource import FortyTwoRessource, RessourceTemplate


class GetProjects(FortyTwoRessource[List[FortyTwoProject]]):
    """
    This class provides a ressource for getting all projects.
    """

    method: str = "GET"
    _url: str = "/projects"

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return [FortyTwoProject(project) for project in response_data]


class GetProjectsById(FortyTwoRessource[FortyTwoProject]):
    """
    This class provides a ressource for getting a project by its ID.
    """

    method: str = "GET"
    _url: str = "/projects/%s"

    def __init__(self: Self, project_id: int) -> None:
        self.project_id = project_id

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url % self.project_id

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return FortyTwoProject(response_data)


class GetProjectsByCursus(FortyTwoRessource[List[FortyTwoProject]]):
    """
    This class provides a ressource for getting all projects for a cursus.
    """

    method: str = "GET"
    _url: str = "/cursus/%s/projects"

    def __init__(self: Self, cursus_id: int) -> None:
        self.cursus_id = cursus_id

    @property
    def url(self: Self) -> str:
        return self.config.endpoint + self._url % self.cursus_id

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return [FortyTwoProject(project) for project in response_data]
