from app.modules.auth.auth_constants import (
    ROLE_PERMISSIONS,
    Permission,
    Role,
    permissions_for,
)


def test_admin_holds_every_user_permission():  # AC16
    assert permissions_for(Role.admin) == {Permission.users_read, Permission.users_read_self}


def test_user_can_only_read_self():  # AC16
    assert permissions_for(Role.user) == {Permission.users_read_self}


def test_every_role_has_a_permission_entry():  # AC16, inferred: new role forgotten in the map
    assert set(ROLE_PERMISSIONS) == set(Role)


def test_unknown_role_has_no_permissions_and_is_logged(app_logs):  # EC21
    assert permissions_for("superuser") == frozenset()

    assert any("superuser" in r.getMessage() and r.levelname == "WARNING" for r in app_logs.records)
