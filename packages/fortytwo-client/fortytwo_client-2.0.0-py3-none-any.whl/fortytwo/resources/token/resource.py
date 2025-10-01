"""
This module provides ressources for getting token information.
"""

from typing import Any, Self

from fortytwo.resources.ressource import FortyTwoRessource, RessourceTemplate
from fortytwo.resources.token.token import FortyTwoToken


class GetToken(FortyTwoRessource[FortyTwoToken]):
    """
    This class provides a ressource for getting token information.
    """

    method: str = "GET"
    _url: str = "https://api.intra.42.fr/oauth/token/info"

    @property
    def url(self: Self) -> str:
        return self._url

    def parse_response(self: Self, response_data: Any) -> RessourceTemplate:
        return FortyTwoToken(response_data)
