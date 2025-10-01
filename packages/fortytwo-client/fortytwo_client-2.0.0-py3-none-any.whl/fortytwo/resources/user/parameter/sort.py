from fortytwo.request.parameter.parameter import Sort


class UserSort:
    """
    Sort class specifically for user resources with all supported 42 API sort fields.
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
    def by_login(direction: str = "asc") -> Sort:
        """
        Sort by login.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-login" if direction == "desc" else "login"
        return Sort([field])

    @staticmethod
    def by_email(direction: str = "asc") -> Sort:
        """
        Sort by email.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-email" if direction == "desc" else "email"
        return Sort([field])

    @staticmethod
    def by_created_at(direction: str = "desc") -> Sort:
        """
        Sort by creation date.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-created_at" if direction == "desc" else "created_at"
        return Sort([field])

    @staticmethod
    def by_updated_at(direction: str = "desc") -> Sort:
        """
        Sort by update date.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-updated_at" if direction == "desc" else "updated_at"
        return Sort([field])

    @staticmethod
    def by_first_name(direction: str = "asc") -> Sort:
        """
        Sort by first name.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-first_name" if direction == "desc" else "first_name"
        return Sort([field])

    @staticmethod
    def by_last_name(direction: str = "asc") -> Sort:
        """
        Sort by last name.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-last_name" if direction == "desc" else "last_name"
        return Sort([field])

    @staticmethod
    def by_pool_year(direction: str = "desc") -> Sort:
        """
        Sort by pool year.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-pool_year" if direction == "desc" else "pool_year"
        return Sort([field])

    @staticmethod
    def by_pool_month(direction: str = "desc") -> Sort:
        """
        Sort by pool month.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-pool_month" if direction == "desc" else "pool_month"
        return Sort([field])

    @staticmethod
    def by_kind(direction: str = "asc") -> Sort:
        """
        Sort by user kind.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-kind" if direction == "desc" else "kind"
        return Sort([field])

    @staticmethod
    def by_status(direction: str = "asc") -> Sort:
        """
        Sort by status.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-status" if direction == "desc" else "status"
        return Sort([field])

    @staticmethod
    def by_last_seen_at(direction: str = "desc") -> Sort:
        """
        Sort by last seen date.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-last_seen_at" if direction == "desc" else "last_seen_at"
        return Sort([field])

    @staticmethod
    def by_alumnized_at(direction: str = "desc") -> Sort:
        """
        Sort by alumnized date.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-alumnized_at" if direction == "desc" else "alumnized_at"
        return Sort([field])
