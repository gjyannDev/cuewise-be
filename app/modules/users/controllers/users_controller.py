from app.core.pagination import PageParams

from ..schemas.users_schema import UserAdminOut, UserListOut
from ..services.users_service import UsersService


class UsersController:
    def __init__(self, service: UsersService):
        self.service = service

    def list_users(self, page: PageParams) -> UserListOut:
        users, total = self.service.list_users(page)
        items = [UserAdminOut.model_validate(user) for user in users]
        return UserListOut(items=items, total=total, limit=page.limit, offset=page.offset)
