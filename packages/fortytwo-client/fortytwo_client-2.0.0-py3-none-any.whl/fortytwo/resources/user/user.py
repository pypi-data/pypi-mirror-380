"""
This module provides ressources for getting project users from the 42 API.
"""

from typing import TYPE_CHECKING, Any, Self

from dateutil.parser import parse as parse_date

from fortytwo.json import register_serializer

if TYPE_CHECKING:
    from datetime import datetime


class FortyTwoUser:
    """
    This class provides a representation of a 42 project user.
    """

    def __init__(self: Self, data: Any) -> None:
        self.id: int = data["id"]
        self.login: str = data["login"]

        self.kind: str = data["kind"]
        self.alumni: bool = data["alumni?"]
        self.active: bool = data["active?"]

        self.image: dict = {
            "large": data["image"]["versions"]["large"],
            "medium": data["image"]["versions"]["medium"],
            "small": data["image"]["versions"]["small"],
            "micro": data["image"]["versions"]["micro"],
        }

        self.created_at: datetime = parse_date(data["created_at"])
        self.updated_at: datetime = parse_date(data["updated_at"])

    def __repr__(self: Self) -> str:
        return f"<FortyTwoUser {self.name}>"

    def __str__(self: Self) -> str:
        return self.name


register_serializer(
    FortyTwoUser,
    lambda u: {
        "id": u.id,
        "login": u.login,
        "kind": u.kind,
        "alumni": u.alumni,
        "active": u.active,
        "image": u.image,
        "created_at": u.created_at.isoformat(),
        "updated_at": u.updated_at.isoformat(),
    },
)
