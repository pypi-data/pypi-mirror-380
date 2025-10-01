"""
Tradelink Authentication Client

Enterprise authentication client for microservices with Kong/Keycloak integration.
"""

from .config import AuthMode, AuthSettings
from .fastapi_utils import (
    get_current_auth,
    get_current_service,
    get_current_user,
    get_optional_auth,
    get_optional_user,
    require_admin,
    require_customer,
    require_moderator,
    require_roles,
    require_scopes,
    require_supplier,
    require_supplier_or_admin,
    require_user_admin,
    require_user_customer,
    require_user_moderator,
    require_user_supplier,
    verify_hmac_signature,
)
from .middleware import AuthMiddleware
from .schemas import ServiceContext, UserContext
from .user_auth import UserValidator

__version__ = "0.2.0"

__all__ = [
    # Configuration
    "AuthSettings",
    "AuthMode",
    # Schemas
    "UserContext",
    "ServiceContext",
    # User Authentication
    "UserValidator",
    # Middleware
    "AuthMiddleware",
    # FastAPI Dependencies
    "get_current_auth",
    "get_current_user",
    "get_current_service",
    "get_optional_auth",
    "get_optional_user",
    "require_roles",
    "require_scopes",
    "require_admin",
    "require_supplier",
    "require_customer",
    "require_moderator",
    "require_supplier_or_admin",
    "verify_hmac_signature",
    "require_user_admin",
    "require_user_customer",
    "require_user_supplier",
    "require_user_moderator",
]
