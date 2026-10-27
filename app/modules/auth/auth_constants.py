import logging
from enum import StrEnum

logger = logging.getLogger("app.auth")


class Role(StrEnum):
    admin = "admin"
    user = "user"


class Permission(StrEnum):
    users_read = "users:read"
    users_read_self = "users:read_self"


# Single source of truth for what each role may do. Edit here to change access.
ROLE_PERMISSIONS: dict[Role, frozenset[Permission]] = {
    Role.admin: frozenset({Permission.users_read, Permission.users_read_self}),
    Role.user: frozenset({Permission.users_read_self}),
}


def permissions_for(role: str) -> frozenset[Permission]:
    """The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later."""
    try:
        return ROLE_PERMISSIONS[Role(role)]
    except (ValueError, KeyError):
        # Default-deny: an unmapped role gets nothing rather than crashing the request.
        logger.warning("Role %r has no permission mapping; denying all permissions", role)
        return frozenset()
