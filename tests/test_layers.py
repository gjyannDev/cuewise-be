"""The layer rules of app/modules (CLAUDE.md, "Architecture"): route -> controller -> service -> repository.

`check_layers` reads source as text and never imports it, so a bad import is reported, not executed.
"""

import ast
from collections.abc import Iterable, Mapping
from pathlib import Path

# Modules already in layer folders; each joins once it is migrated (see docs/features/layered-modules/plan.md).
MIGRATED: tuple[str, ...] = ("auth", "users", "interviews")


def check_layers(files: Mapping[str, str], modules: Iterable[str] | None = None) -> list[str]:
    """Every layer-rule violation in `files` (repo-relative path -> source), as "<path>: <what>" lines.
    `modules` limits the check to those features; None checks every file given."""
    wanted = None if modules is None else set(modules)
    violations: list[str] = []
    for path, source in sorted(files.items()):
        parts = path.removesuffix(".py").split("/")
        if parts[:2] != ["app", "modules"] or len(parts) < 4:
            continue
        feature = parts[2]
        if wanted is not None and feature not in wanted:
            continue
        if len(parts) == 4 and parts[3] != "__init__":
            violations.append(f"{path}: file at the module root; move it into a layer folder")
            continue
        layer = parts[3] if len(parts) > 4 else None
        package = parts[:-1]
        for module, names in _imports(source, package):
            message = _violation(feature, layer, module, names)
            if message:
                violations.append(f"{path}: {message}")
    return violations


def _imports(source: str, package: list[str]) -> list[tuple[str, list[str]]]:
    """(absolute module, imported names) per import statement; relative imports resolved against `package`."""
    found: list[tuple[str, list[str]]] = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            found.extend((alias.name, []) for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            base = package[: len(package) - node.level + 1] if node.level else []
            module = ".".join([*base, *([node.module] if node.module else [])])
            found.append((module, [alias.name for alias in node.names]))
    return found


_FORBIDDEN = {
    "routes": {"services", "repositories"},
    "controllers": {"repositories"},
    "services": {"controllers", "routes"},
    "repositories": {"services", "controllers", "routes"},
}


def _violation(feature: str, layer: str | None, module: str, names: list[str]) -> str | None:
    kind = {"routes": "route", "controllers": "controller", "services": "service", "repositories": "repository"}
    target = module.split(".")
    target_feature = target[2] if target[:2] == ["app", "modules"] and len(target) > 3 else None
    target_folder = target[3] if target_feature else None
    if layer in _FORBIDDEN and target_folder in _FORBIDDEN[layer]:
        return f"{kind[layer]} imports {module}"
    if layer == "controllers" and module.startswith(("app.core.ai", "app.db.session")):
        return f"controller imports {module}"
    if layer == "services" and target_folder == "schemas":
        responses = [name for name in names if name.endswith("Out")]
        if responses:
            return f"service imports response schema {', '.join(responses)}"
    if target_feature and target_feature != feature and target_folder == "repositories":
        return f"{feature} imports another feature's repository {module}"
    return None


# --- synthetic sources: one rule each ---

AUTH = "app/modules/auth"


def _one(path: str, source: str) -> list[str]:
    return check_layers({path: source})


def test_clean_layer_imports_have_no_violations():
    files = {
        f"{AUTH}/routes/auth_route.py": "from ..controllers.auth_controller import AuthControllerDep\n"
        "from app.modules.auth.dependencies.auth_dependencies import require_permissions\n",
        f"{AUTH}/controllers/auth_controller.py": "from ..services.auth_service import AuthService\n"
        "from ..schemas.auth_schema import MeOut\n",
        f"{AUTH}/services/auth_service.py": "from ..repositories.auth_repository import AuthRepository\n"
        "from ..schemas.auth_schema import LoginIn\n",
        f"{AUTH}/repositories/auth_repository.py": "from ..models.auth_model import User\n",
        f"{AUTH}/__init__.py": "",
    }
    assert check_layers(files) == []


def test_route_importing_a_service_or_repository_is_reported():
    path = f"{AUTH}/routes/auth_route.py"
    assert _one(path, "from ..services.auth_service import AuthService\n") == [
        f"{path}: route imports app.modules.auth.services.auth_service"
    ]
    assert _one(path, "import app.modules.auth.repositories.auth_repository\n") == [
        f"{path}: route imports app.modules.auth.repositories.auth_repository"
    ]


def test_controller_importing_a_repository_the_llm_or_the_db_session_is_reported():
    path = f"{AUTH}/controllers/auth_controller.py"
    assert _one(path, "from ..repositories.auth_repository import AuthRepository\n") == [
        f"{path}: controller imports app.modules.auth.repositories.auth_repository"
    ]
    assert _one(path, "from app.core.ai.provider import LLMProvider\n") == [
        f"{path}: controller imports app.core.ai.provider"
    ]
    assert _one(path, "from app.db.session import get_db\n") == [f"{path}: controller imports app.db.session"]


def test_service_importing_a_controller_or_route_is_reported():
    path = f"{AUTH}/services/auth_service.py"
    assert _one(path, "from ..controllers.auth_controller import AuthController\n") == [
        f"{path}: service imports app.modules.auth.controllers.auth_controller"
    ]
    assert _one(path, "from app.modules.auth.routes import auth_route\n") == [
        f"{path}: service imports app.modules.auth.routes"
    ]


def test_service_importing_a_response_schema_is_reported():
    path = f"{AUTH}/services/auth_service.py"
    assert _one(path, "from ..schemas.auth_schema import LoginIn, MeOut\n") == [
        f"{path}: service imports response schema MeOut"
    ]


def test_repository_importing_a_service_controller_or_route_is_reported():
    path = f"{AUTH}/repositories/auth_repository.py"
    assert _one(path, "from ..services.auth_service import AuthService\n") == [
        f"{path}: repository imports app.modules.auth.services.auth_service"
    ]
    assert _one(path, "from ..controllers.auth_controller import AuthController\n") == [
        f"{path}: repository imports app.modules.auth.controllers.auth_controller"
    ]
    assert _one(path, "from ..routes.auth_route import router\n") == [
        f"{path}: repository imports app.modules.auth.routes.auth_route"
    ]


def test_a_feature_importing_another_features_repository_is_reported():
    path = "app/modules/interviews/dependencies/interviews_start_dependencies.py"
    assert _one(path, "from app.modules.auth.repositories.auth_repository import AuthRepository\n") == [
        f"{path}: interviews imports another feature's repository app.modules.auth.repositories.auth_repository"
    ]


def test_a_layer_file_left_at_a_module_root_is_reported():
    assert _one(f"{AUTH}/auth_controller.py", "") == [
        f"{AUTH}/auth_controller.py: file at the module root; move it into a layer folder"
    ]


def test_the_real_tree_follows_the_layer_rules():
    root = Path(__file__).resolve().parents[1]
    files = {
        p.relative_to(root).as_posix(): p.read_text(encoding="utf-8")
        for m in MIGRATED
        for p in (root / "app" / "modules" / m).rglob("*.py")
    }
    assert check_layers(files, MIGRATED) == []
