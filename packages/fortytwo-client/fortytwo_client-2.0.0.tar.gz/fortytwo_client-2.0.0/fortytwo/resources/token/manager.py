from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from fortytwo.resources.token.resource import GetToken

if TYPE_CHECKING:
    from fortytwo.client import FortyTwoClient
    from fortytwo.request.params import FortyTwoParam
    from fortytwo.resources.token.token import FortyTwoToken


class TokenManager:
    """
    Manager for token-related API operations.
    """

    def __init__(self, client: FortyTwoClient) -> None:
        self._client = client

    def get(self, *params: FortyTwoParam) -> Optional[FortyTwoToken]:
        """
        Get token information.

        Args:
            *params: Additional request parameters

        Returns:
            FortyTwoToken object or None if request failed
        """
        return self._client.request(GetToken(), *params)
