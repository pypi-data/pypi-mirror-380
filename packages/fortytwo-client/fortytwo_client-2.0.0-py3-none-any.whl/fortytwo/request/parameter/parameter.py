from datetime import datetime
from typing import List, Self, Tuple, Union


class FortyTwoParam:
    """
    This class provides a base for query parameters.
    """

    @staticmethod
    def _serialize_to_string(value: Union[str, int, datetime, None]) -> str:
        if value is None:
            return ""
        elif isinstance(value, datetime):
            return value.isoformat()
        else:
            return str(value)

    def to_query_param(self: Self) -> Tuple[str, str]:
        """
        Returns the query parameter string representation of the object.

        Returns:
            str: The query parameter string representation.
        """

        raise NotImplementedError


class Parameter(FortyTwoParam):
    """
    This class provides a generic query parameter.
    """

    def __init__(self: Self, name: str, value: Union[str, int, datetime]) -> None:
        self.name = name
        self.value = value

    def to_query_param(self: Self) -> Tuple[str, str]:
        return (self.name, self._serialize_to_string(self.value))


class Sort(FortyTwoParam):
    """
    This class provides a sort query parameter.
    """

    def __init__(self: Self, by: List[str]) -> None:
        self.by = by

    def to_query_param(self: Self) -> Tuple[str, str]:
        return ("sort", ",".join(self.by))


class Filter(FortyTwoParam):
    """
    This class provides a filter query parameter.
    """

    def __init__(self: Self, by: str, values: List[Union[str, int, datetime]]) -> None:
        self.by = by
        self.values = values

    def to_query_param(self: Self) -> Tuple[str, str]:
        values = [self._serialize_to_string(v) for v in self.values]
        return (f"filter[{self.by}]", ",".join(values))


class Range(FortyTwoParam):
    """
    This class provides a range query parameter.
    """

    def __init__(self: Self, by: str, values: List[Union[str, int, datetime]]) -> None:
        self.by = by
        self.values = values

    def to_query_param(self: Self) -> Tuple[str, str]:
        values = [self._serialize_to_string(v) for v in self.values]
        return (f"range[{self.by}]", ",".join(values))


class PageNumber(FortyTwoParam):
    """
    This class provides a range query parameter.
    """

    def __init__(self: Self, page_number: int) -> None:
        self.page_number = page_number

    def to_query_param(self: Self) -> Tuple[str, str]:
        return ("page[number]", str(self.page_number))


class PageSize(FortyTwoParam):
    """
    This class provides a range query parameter.
    """

    def __init__(self: Self, page_size: int) -> None:
        if page_size < 1 or page_size > 100:
            raise ValueError("Page size must be between 1 and 100.")

        self.page_size = page_size

    def to_query_param(self: Self) -> Tuple[str, str]:
        return ("page[size]", str(self.page_size))
