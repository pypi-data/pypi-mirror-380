"""
This module provides ressources for getting token information.
"""

from typing import Any, List, Optional, Self

from fortytwo.json import register_serializer


class FortyTwoToken:
    """
    This class provides a representation of a token
    """

    def __init__(self: Self, data: Any) -> None:
        self.owner: Optional[int] = data["resource_owner_id"]
        self.scopes: List[str] = data["scopes"]

        self.expires: int = data["expires_in_seconds"]
        self.uid: str = data["application"]["uid"]

    def __repr__(self: Self) -> str:
        return f"<FortyTwoToken {self.uid}>"

    def __str__(self: Self) -> str:
        return self.uid


register_serializer(
    FortyTwoToken,
    lambda p: {
        "owner": p.owner,
        "scopes": p.scopes,
        "expires": p.expires,
        "uid": p.uid,
    },
)
