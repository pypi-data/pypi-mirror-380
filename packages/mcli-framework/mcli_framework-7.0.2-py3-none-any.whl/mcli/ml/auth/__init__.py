"""Authentication and authorization system"""

from .auth_manager import (
    AuthManager,
    create_access_token,
    verify_access_token,
    get_current_user,
    get_current_active_user,
    require_role,
    hash_password,
    verify_password,
)
from .models import (
    UserCreate,
    UserLogin,
    UserResponse,
    TokenResponse,
    PasswordReset,
    PasswordChange,
)
from .permissions import (
    Permission,
    check_permission,
    has_permission,
)

__all__ = [
    "AuthManager",
    "create_access_token",
    "verify_access_token",
    "get_current_user",
    "get_current_active_user",
    "require_role",
    "hash_password",
    "verify_password",
    "UserCreate",
    "UserLogin",
    "UserResponse",
    "TokenResponse",
    "PasswordReset",
    "PasswordChange",
    "Permission",
    "check_permission",
    "has_permission",
]