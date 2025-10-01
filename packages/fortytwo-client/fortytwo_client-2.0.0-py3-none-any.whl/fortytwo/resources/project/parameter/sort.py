from fortytwo.request.parameter.parameter import Sort


class ProjectSort:
    """
    Sort class specifically for project resources with all supported 42 API sort fields.
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
    def by_name(direction: str = "asc") -> Sort:
        """
        Sort by name.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-name" if direction == "desc" else "name"
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
    def by_visible(direction: str = "desc") -> Sort:
        """
        Sort by visibility status.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-visible" if direction == "desc" else "visible"
        return Sort([field])

    @staticmethod
    def by_exam(direction: str = "desc") -> Sort:
        """
        Sort by exam status.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-exam" if direction == "desc" else "exam"
        return Sort([field])

    @staticmethod
    def by_parent_id(direction: str = "asc") -> Sort:
        """
        Sort by parent ID.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-parent_id" if direction == "desc" else "parent_id"
        return Sort([field])

    @staticmethod
    def by_slug(direction: str = "asc") -> Sort:
        """
        Sort by slug.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-slug" if direction == "desc" else "slug"
        return Sort([field])

    @staticmethod
    def by_inherited_team(direction: str = "desc") -> Sort:
        """
        Sort by inherited team status.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-inherited_team" if direction == "desc" else "inherited_team"
        return Sort([field])

    @staticmethod
    def by_position(direction: str = "asc") -> Sort:
        """
        Sort by position.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-position" if direction == "desc" else "position"
        return Sort([field])

    @staticmethod
    def by_has_git(direction: str = "desc") -> Sort:
        """
        Sort by git availability.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-has_git" if direction == "desc" else "has_git"
        return Sort([field])

    @staticmethod
    def by_has_mark(direction: str = "desc") -> Sort:
        """
        Sort by mark availability.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-has_mark" if direction == "desc" else "has_mark"
        return Sort([field])

    @staticmethod
    def by_repository(direction: str = "asc") -> Sort:
        """
        Sort by repository.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-repository" if direction == "desc" else "repository"
        return Sort([field])

    @staticmethod
    def by_git_id(direction: str = "asc") -> Sort:
        """
        Sort by git ID.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = "-git_id" if direction == "desc" else "git_id"
        return Sort([field])

    @staticmethod
    def by_cached_repository_path(direction: str = "asc") -> Sort:
        """
        Sort by cached repository path.

        Args:
            direction (str): Sort direction ("asc" or "desc").
        """
        field = (
            "-cached_repository_path"
            if direction == "desc"
            else "cached_repository_path"
        )
        return Sort([field])
