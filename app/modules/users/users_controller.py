from .users_repository import UsersRepository
from .users_schema import UserAdminOut, UserListOut


class UsersController:
    def __init__(self, repo: UsersRepository):
        self.repo = repo

    def list_users(self, limit: int, offset: int) -> UserListOut:
        items = [UserAdminOut.model_validate(user) for user in self.repo.list(limit, offset)]
        return UserListOut(items=items, total=self.repo.count(), limit=limit, offset=offset)
