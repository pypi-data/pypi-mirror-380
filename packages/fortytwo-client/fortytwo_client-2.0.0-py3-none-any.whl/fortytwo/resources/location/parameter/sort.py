from fortytwo.request.parameter.parameter import Sort


class LocationSort:
    """
    Sort class specifically for location resources with all supported 42 API sort fields.
    """

    @staticmethod
    def by_id(direction: str = "desc") -> Sort:
        """
        Sort by ID (default descending).

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-id" if direction == "desc" else "id"
        return Sort([field])

    @staticmethod
    def by_user_id(direction: str = "asc") -> Sort:
        """
        Sort by user ID.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-user_id" if direction == "desc" else "user_id"
        return Sort([field])

    @staticmethod
    def by_begin_at(direction: str = "desc") -> Sort:
        """
        Sort by begin date.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-begin_at" if direction == "desc" else "begin_at"
        return Sort([field])

    @staticmethod
    def by_end_at(direction: str = "desc") -> Sort:
        """
        Sort by end date.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-end_at" if direction == "desc" else "end_at"
        return Sort([field])

    @staticmethod
    def by_primary(direction: str = "desc") -> Sort:
        """
        Sort by primary status.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-primary" if direction == "desc" else "primary"
        return Sort([field])

    @staticmethod
    def by_host(direction: str = "asc") -> Sort:
        """
        Sort by host.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-host" if direction == "desc" else "host"
        return Sort([field])

    @staticmethod
    def by_campus_id(direction: str = "asc") -> Sort:
        """
        Sort by campus ID.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-campus_id" if direction == "desc" else "campus_id"
        return Sort([field])
