"""The signed-in user's résumé profile: request -> ProfileService, stored row -> ProfileOut."""

from app.modules.auth.models.auth_model import User

from ..models.profile_model import CandidateProfileRow
from ..schemas.profile_schema import ProfileOut
from ..services.profile_service import ProfileService


def _out(row: CandidateProfileRow) -> ProfileOut:
    return ProfileOut.model_validate({**row.profile, "updated_at": row.updated_at})


class ProfileController:
    def __init__(self, service: ProfileService):
        self.service = service

    def upload(self, user: User, data: bytes) -> ProfileOut:
        return _out(self.service.upload(user, data))

    def get(self, user: User) -> ProfileOut:
        return _out(self.service.get(user))

    def delete(self, user: User) -> None:
        self.service.delete(user)
