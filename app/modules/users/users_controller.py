from app.core.pagination import PageParams

from .users_repository import UsersRepository
from .users_schema import UserAdminOut, UserListOut


class UsersController:
    def __init__(self, repo: UsersRepository):
        self.repo = repo

    def list_users(self, page: PageParams) -> UserListOut:
        items = [UserAdminOut.model_validate(user) for user in self.repo.list(page.limit, page.offset)]
        return UserListOut(items=items, total=self.repo.count(), limit=page.limit, offset=page.offset)
