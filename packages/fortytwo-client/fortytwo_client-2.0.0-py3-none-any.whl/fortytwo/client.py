from __future__ import annotations

import time
from typing import TYPE_CHECKING, Optional, Self

from requests.exceptions import HTTPError, RequestException

from fortytwo.config import FortyTwoConfig
from fortytwo.logger import logger
from fortytwo.request import FortyTwoRequest
from fortytwo.request.authentication import (
    FortyTwoAuthentication,
    FortyTwoSecrets,
    FortyTwoTokens,
)
from fortytwo.resources.location import LocationManager
from fortytwo.resources.project import ProjectManager
from fortytwo.resources.project_user import ProjectUserManager
from fortytwo.resources.ressource import FortyTwoRessource, RessourceTemplate
from fortytwo.resources.token import TokenManager
from fortytwo.resources.user import UserManager

if TYPE_CHECKING:
    from requests import Response

    from fortytwo.request.parameter.parameter import FortyTwoParam


class FortyTwoClient:
    """
    This class provides a client for the 42 School API.
    """

    config: FortyTwoConfig
    secrets: FortyTwoSecrets

    _tokens: Optional[FortyTwoTokens] = None
    _request: FortyTwoRequest[RessourceTemplate]

    _is_rate_limited: bool = False
    _request_time: float

    def __init__(
        self: Self,
        client_id: str,
        client_secret: str,
        config: Optional[FortyTwoConfig] = None,
    ) -> None:
        self.config = config or FortyTwoConfig()
        self.secrets = FortyTwoSecrets(client_id, client_secret)

        self.users = UserManager(self)
        self.locations = LocationManager(self)
        self.projects = ProjectManager(self)
        self.project_users = ProjectUserManager(self)
        self.tokens = TokenManager(self)

    def request(
        self: Self,
        ressource: FortyTwoRessource[RessourceTemplate],
        *params: FortyTwoParam,
    ) -> RessourceTemplate:
        """
        This function sends a request to the API and returns the response

        Args:
            ressource (FortyTwoRessource): The ressource to fetch.
            params (FortyTwoParam): The parameters for the request.

        Returns:
            U: The response from the API.
        """

        if self._tokens is None:
            self._tokens = FortyTwoAuthentication.get_tokens(self.secrets)

        self._request = FortyTwoRequest[RessourceTemplate](
            ressource.set_config(self.config), *params
        )

        return self._make_request()

    def _make_request(self: Self) -> Optional[RessourceTemplate]:
        self._request_time = time.perf_counter()

        try:
            response = self._request.request(self._tokens)
            self._request.rate_limit(
                self._request_time, self.config.rate_limit_per_second
            )

            self._is_rate_limited = False
            return response

        except HTTPError as e:
            self._request.rate_limit(
                self._request_time, self.config.rate_limit_per_second
            )
            return self._handle_http_exception(e.response)

        except RequestException as e:
            logger.error("Failed to fetch from the API: %s", e)
            return self._make_request()

    def _handle_rate_limit(self: Self) -> Optional[RessourceTemplate]:
        if self._is_rate_limited:
            logger.error("Rate limit exceeded again, retrying in 5 minutes...")
            time.sleep(300)
        else:
            logger.warning("Rate limit exceeded, retrying.")
            time.sleep(1)

        self._is_rate_limited = True

        return self._make_request()

    def _handle_unauthorized(
        self: Self, response: Response
    ) -> Optional[RessourceTemplate]:
        logger.info("Access token expired, fetching a new one.")

        self._tokens = FortyTwoAuthentication.get_tokens(self.secrets)

        return self._make_request()

    def _handle_http_exception(
        self: Self, response: Response
    ) -> Optional[RessourceTemplate]:
        if response.status_code == 429:
            return self._handle_rate_limit()

        self._is_rate_limited = False

        logger.error(
            "Failed to fetch from the API (%s): %s.",
            response.status_code,
            response.reason,
        )

        if response.status_code == 401:
            return self._handle_unauthorized(response)

        return None
