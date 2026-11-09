from collections.abc import Sequence

from app.core.pagination import PageParams
from app.modules.auth.models.auth_model import User

from ..repositories.users_repository import UsersRepository


class UsersService:
    def __init__(self, repo: UsersRepository):
        self.repo = repo

    def list_users(self, page: PageParams) -> tuple[Sequence[User], int]:
        """One page of users and the total count."""
        return self.repo.list(page.limit, page.offset), self.repo.count()
