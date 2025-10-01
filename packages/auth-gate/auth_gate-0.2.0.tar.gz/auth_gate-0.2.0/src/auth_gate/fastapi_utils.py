"""
FastAPI dependency injection utilities for authentication (User and Service)
"""

import logging
from typing import Optional

from fastapi import Depends, Header, HTTPException, Request, status

from .config import get_settings
from .schemas import AuthContext, ServiceContext, UserContext
from .user_auth import HMACVerifier, get_user_validator

logger = logging.getLogger(__name__)


# Core authentication dependencies
async def get_current_auth(
    request: Request,
    authorization: Optional[str] = Header(None),
    x_token_verified: Optional[str] = Header(None, alias="X-Token-Verified"),
    x_auth_source: Optional[str] = Header(None, alias="X-Auth-Source"),
    # User headers
    x_user_id: Optional[str] = Header(None, alias="X-User-ID"),
    x_username: Optional[str] = Header(None, alias="X-Username"),
    x_user_email: Optional[str] = Header(None, alias="X-User-Email"),
    x_user_roles: Optional[str] = Header(None, alias="X-User-Roles"),
    x_user_scopes: Optional[str] = Header(None, alias="X-User-Scopes"),
    # Service headers
    x_service_name: Optional[str] = Header(None, alias="X-Service-Name"),
    x_service_authenticated: Optional[str] = Header(None, alias="X-Service-Authenticated"),
    x_service_roles: Optional[str] = Header(None, alias="X-Service-Roles"),
    # Common headers
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_client_id: Optional[str] = Header(None, alias="X-Client-ID"),
) -> AuthContext:
    """
    Main dependency for getting authenticated user or service.

    Returns either UserContext or ServiceContext based on the authentication type.

    Example:
        @app.get("/api/resource")
        async def get_resource(auth: AuthContext = Depends(get_current_auth)):
            if isinstance(auth, UserContext):
                return {"user_id": auth.user_id}
            elif isinstance(auth, ServiceContext):
                return {"service": auth.service_name}

    Args:
        Various authentication headers for both users and services

    Returns:
        AuthContext (UserContext or ServiceContext) with authenticated information

    Raises:
        HTTPException: If authentication fails
    """
    validator = get_user_validator()
    return await validator.get_current_user(
        request,
        authorization,
        x_token_verified,
        x_auth_source,
        x_user_id,
        x_username,
        x_user_email,
        x_user_roles,
        x_user_scopes,
        x_service_name,
        x_service_authenticated,
        x_service_roles,
        x_session_id,
        x_client_id,
    )


async def get_current_user(
    request: Request,
    authorization: Optional[str] = Header(None),
    x_token_verified: Optional[str] = Header(None, alias="X-Token-Verified"),
    x_auth_source: Optional[str] = Header(None, alias="X-Auth-Source"),
    x_user_id: Optional[str] = Header(None, alias="X-User-ID"),
    x_username: Optional[str] = Header(None, alias="X-Username"),
    x_user_email: Optional[str] = Header(None, alias="X-User-Email"),
    x_user_roles: Optional[str] = Header(None, alias="X-User-Roles"),
    x_user_scopes: Optional[str] = Header(None, alias="X-User-Scopes"),
    x_service_name: Optional[str] = Header(None, alias="X-Service-Name"),
    x_service_authenticated: Optional[str] = Header(None, alias="X-Service-Authenticated"),
    x_service_roles: Optional[str] = Header(None, alias="X-Service-Roles"),
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_client_id: Optional[str] = Header(None, alias="X-Client-ID"),
) -> UserContext:
    """
    Dependency for getting authenticated user (user-only, rejects services).

    This enforces that the request must be from a user, not a service.

    Example:
        @app.get("/api/profile")
        async def get_profile(user: UserContext = Depends(get_current_user)):
            return {"user_id": user.user_id}

    Args:
        Various authentication headers

    Returns:
        UserContext with authenticated user information

    Raises:
        HTTPException: If authentication fails or if authenticated as service
    """
    auth = await get_current_auth(
        request,
        authorization,
        x_token_verified,
        x_auth_source,
        x_user_id,
        x_username,
        x_user_email,
        x_user_roles,
        x_user_scopes,
        x_service_name,
        x_service_authenticated,
        x_service_roles,
        x_session_id,
        x_client_id,
    )

    if isinstance(auth, ServiceContext):
        logger.warning(f"Service {auth.service_name} attempted to access user-only endpoint")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This endpoint requires user authentication",
        )

    return auth


async def get_current_service(
    request: Request,
    authorization: Optional[str] = Header(None),
    x_token_verified: Optional[str] = Header(None, alias="X-Token-Verified"),
    x_auth_source: Optional[str] = Header(None, alias="X-Auth-Source"),
    x_user_id: Optional[str] = Header(None, alias="X-User-ID"),
    x_username: Optional[str] = Header(None, alias="X-Username"),
    x_user_email: Optional[str] = Header(None, alias="X-User-Email"),
    x_user_roles: Optional[str] = Header(None, alias="X-User-Roles"),
    x_user_scopes: Optional[str] = Header(None, alias="X-User-Scopes"),
    x_service_name: Optional[str] = Header(None, alias="X-Service-Name"),
    x_service_authenticated: Optional[str] = Header(None, alias="X-Service-Authenticated"),
    x_service_roles: Optional[str] = Header(None, alias="X-Service-Roles"),
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_client_id: Optional[str] = Header(None, alias="X-Client-ID"),
) -> ServiceContext:
    """
    Dependency for getting authenticated service (service-only, rejects users).

    This enforces that the request must be from a service, not a user.

    Example:
        @app.post("/api/internal/sync")
        async def sync_data(service: ServiceContext = Depends(get_current_service)):
            return {"service": service.service_name}

    Args:
        Various authentication headers

    Returns:
        ServiceContext with authenticated service information

    Raises:
        HTTPException: If authentication fails or if authenticated as user
    """
    auth = await get_current_auth(
        request,
        authorization,
        x_token_verified,
        x_auth_source,
        x_user_id,
        x_username,
        x_user_email,
        x_user_roles,
        x_user_scopes,
        x_service_name,
        x_service_authenticated,
        x_service_roles,
        x_session_id,
        x_client_id,
    )

    if isinstance(auth, UserContext):
        logger.warning(f"User {auth.user_id} attempted to access service-only endpoint")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This endpoint requires service authentication",
        )

    return auth


async def get_optional_auth(
    request: Request,
    authorization: Optional[str] = Header(None),
    x_token_verified: Optional[str] = Header(None, alias="X-Token-Verified"),
    x_auth_source: Optional[str] = Header(None, alias="X-Auth-Source"),
    x_user_id: Optional[str] = Header(None, alias="X-User-ID"),
    x_username: Optional[str] = Header(None, alias="X-Username"),
    x_user_email: Optional[str] = Header(None, alias="X-User-Email"),
    x_user_roles: Optional[str] = Header(None, alias="X-User-Roles"),
    x_user_scopes: Optional[str] = Header(None, alias="X-User-Scopes"),
    x_service_name: Optional[str] = Header(None, alias="X-Service-Name"),
    x_service_authenticated: Optional[str] = Header(None, alias="X-Service-Authenticated"),
    x_service_roles: Optional[str] = Header(None, alias="X-Service-Roles"),
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_client_id: Optional[str] = Header(None, alias="X-Client-ID"),
) -> Optional[AuthContext]:
    """
    Optional authentication - returns None if not authenticated.

    Use this for endpoints where authentication is optional for both users and services.

    Example:
        @app.get("/api/products")
        async def list_products(auth: Optional[AuthContext] = Depends(get_optional_auth)):
            if auth:
                # Show personalized products
                pass
            else:
                # Show public products
                pass

    Args:
        Various authentication headers

    Returns:
        AuthContext (UserContext or ServiceContext) if authenticated, None otherwise
    """
    try:
        return await get_current_auth(
            request,
            authorization,
            x_token_verified,
            x_auth_source,
            x_user_id,
            x_username,
            x_user_email,
            x_user_roles,
            x_user_scopes,
            x_service_name,
            x_service_authenticated,
            x_service_roles,
            x_session_id,
            x_client_id,
        )
    except HTTPException:
        return None


async def get_optional_user(
    request: Request,
    authorization: Optional[str] = Header(None),
    x_token_verified: Optional[str] = Header(None, alias="X-Token-Verified"),
    x_auth_source: Optional[str] = Header(None, alias="X-Auth-Source"),
    x_user_id: Optional[str] = Header(None, alias="X-User-ID"),
    x_username: Optional[str] = Header(None, alias="X-Username"),
    x_user_email: Optional[str] = Header(None, alias="X-User-Email"),
    x_user_roles: Optional[str] = Header(None, alias="X-User-Roles"),
    x_user_scopes: Optional[str] = Header(None, alias="X-User-Scopes"),
    x_service_name: Optional[str] = Header(None, alias="X-Service-Name"),
    x_service_authenticated: Optional[str] = Header(None, alias="X-Service-Authenticated"),
    x_service_roles: Optional[str] = Header(None, alias="X-Service-Roles"),
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_client_id: Optional[str] = Header(None, alias="X-Client-ID"),
) -> Optional[UserContext]:
    """
    Optional user authentication - returns None if not authenticated or if service.

    Use this for endpoints where user authentication is optional but services are ignored.

    Example:
        @app.get("/api/user/recommendations")
        async def get_recommendations(user: Optional[UserContext] = Depends(get_optional_user)):
            if user:
                # Show personalized recommendations
                pass
            else:
                # Show general recommendations
                pass

    Args:
        Various authentication headers

    Returns:
        UserContext if authenticated as user, None otherwise (including if service)
    """
    try:
        auth = await get_current_auth(
            request,
            authorization,
            x_token_verified,
            x_auth_source,
            x_user_id,
            x_username,
            x_user_email,
            x_user_roles,
            x_user_scopes,
            x_service_name,
            x_service_authenticated,
            x_service_roles,
            x_session_id,
            x_client_id,
        )
        if isinstance(auth, UserContext):
            return auth
        return None
    except HTTPException:
        return None


# Role-based access control factories
def require_roles(*required_roles: str):
    """
    Factory for role-checking dependencies.

    Creates a dependency that ensures the user/service has at least one of the specified roles.
    Works with both UserContext and ServiceContext.

    Example:
        require_editor = require_roles("editor", "admin")

        @app.post("/api/articles")
        async def create_article(auth: AuthContext = Depends(require_editor)):
            if isinstance(auth, UserContext):
                return {"created_by": auth.user_id}
            else:
                return {"created_by_service": auth.service_name}

    Args:
        *required_roles: Variable number of role names

    Returns:
        Dependency function that validates roles
    """

    async def role_checker(auth: AuthContext = Depends(get_current_auth)) -> AuthContext:
        if not auth.has_any_role(list(required_roles)):
            identifier = auth.user_id if isinstance(auth, UserContext) else auth.service_name
            logger.warning(f"Auth {identifier} lacks required roles: {required_roles}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires one of roles: {', '.join(required_roles)}",
            )
        return auth

    return role_checker


def require_user_roles(*required_roles: str):
    """
    Factory for user-only role-checking dependencies.

    Creates a dependency that ensures the USER has at least one of the specified roles.
    Services are rejected even if they have the role.

    Example:
        require_user_editor = require_user_roles("editor", "admin")

        @app.post("/api/user/articles")
        async def create_article(user: UserContext = Depends(require_user_editor)):
            return {"created_by": user.user_id}

    Args:
        *required_roles: Variable number of role names

    Returns:
        Dependency function that validates user roles
    """

    async def role_checker(user: UserContext = Depends(get_current_user)) -> UserContext:
        if not user.has_any_role(list(required_roles)):
            logger.warning(f"User {user.user_id} lacks required roles: {required_roles}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires one of roles: {', '.join(required_roles)}",
            )
        return user

    return role_checker


def require_service_roles(*required_roles: str):
    """
    Factory for service-only role-checking dependencies.

    Creates a dependency that ensures the SERVICE has at least one of the specified roles.
    Users are rejected even if they have the role.

    Example:
        require_data_processor = require_service_roles("data-processor", "admin")

        @app.post("/api/internal/process")
        async def process_data(service: ServiceContext = Depends(require_data_processor)):
            return {"processed_by": service.service_name}

    Args:
        *required_roles: Variable number of role names

    Returns:
        Dependency function that validates service roles
    """

    async def role_checker(
        service: ServiceContext = Depends(get_current_service),
    ) -> ServiceContext:
        if not service.has_any_role(list(required_roles)):
            logger.warning(f"Service {service.service_name} lacks required roles: {required_roles}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires one of roles: {', '.join(required_roles)}",
            )
        return service

    return role_checker


def require_scopes(*required_scopes: str):
    """
    Factory for scope-checking dependencies (user-only).

    Creates a dependency that ensures the USER has all specified scopes.
    Services don't have scopes, so they are automatically rejected.

    Example:
        require_write = require_scopes("write", "publish")

        @app.post("/api/publish")
        async def publish(user: UserContext = Depends(require_write)):
            return {"published_by": user.user_id}

    Args:
        *required_scopes: Variable number of scope names

    Returns:
        Dependency function that validates scopes
    """

    async def scope_checker(user: UserContext = Depends(get_current_user)) -> UserContext:
        missing_scopes = [s for s in required_scopes if not user.has_scope(s)]
        if missing_scopes:
            logger.warning(f"User {user.user_id} lacks required scopes: {missing_scopes}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires scopes: {', '.join(missing_scopes)}",
            )
        return user

    return scope_checker


# Pre-configured role dependencies for common use cases (work with both users and services)
require_admin = require_roles("admin")
"""Dependency that requires admin role (user or service)"""

require_supplier = require_roles("supplier")
"""Dependency that requires supplier role (user or service)"""

require_customer = require_roles("customer")
"""Dependency that requires customer role (user or service)"""

require_moderator = require_roles("moderator")
"""Dependency that requires moderator role (user or service)"""

require_supplier_or_admin = require_roles("supplier", "admin")
"""Dependency that requires either supplier or admin role (user or service)"""

# Pre-configured user-only role dependencies
require_user_admin = require_user_roles("admin")
"""Dependency that requires admin role (user only)"""

require_user_supplier = require_user_roles("supplier")
"""Dependency that requires supplier role (user only)"""

require_user_customer = require_user_roles("customer")
"""Dependency that requires customer role (user only)"""

require_user_moderator = require_user_roles("moderator")
"""Dependency that requires moderator role (user only)"""


# HMAC verification for service-to-service communication
async def verify_hmac_signature(
    request: Request,
    x_authz_signature: Optional[str] = Header(None, alias="X-Authz-Signature"),
    x_authz_ts: Optional[str] = Header(None, alias="X-Authz-Ts"),
    auth: AuthContext = Depends(get_current_auth),
) -> AuthContext:
    """
    Dependency to verify HMAC signatures from Kong.

    Use this when Kong is configured with HMAC plugin for additional security.
    Works with both user and service authentication.

    Example:
        @app.post("/api/sensitive")
        async def sensitive_operation(auth: AuthContext = Depends(verify_hmac_signature)):
            if isinstance(auth, UserContext):
                return {"verified_user": auth.user_id}
            else:
                return {"verified_service": auth.service_name}

    Args:
        request: FastAPI request
        x_authz_signature: HMAC signature header
        x_authz_ts: Timestamp header
        auth: Authenticated user or service context

    Returns:
        AuthContext if HMAC is valid

    Raises:
        HTTPException: If HMAC verification fails
    """
    settings = get_settings()

    if not settings.VERIFY_HMAC:
        return auth

    if not x_authz_signature or not x_authz_ts:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing HMAC headers",
        )

    verifier = HMACVerifier(settings.INTERNAL_HMAC_KEY)

    # Get the identifier for HMAC verification
    if isinstance(auth, UserContext):
        identifier = auth.user_id
    else:
        identifier = auth.service_name

    if not verifier.verify_signature(
        x_authz_signature,
        x_authz_ts,
        identifier,
        auth.session_id or "",
        request.method,
        request.url.path,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid HMAC signature",
        )

    return auth


# Utility functions for checking authentication mode
def is_using_kong() -> bool:
    """Check if using Kong authentication"""
    settings = get_settings()
    return settings.is_production


def is_using_keycloak() -> bool:
    """Check if using direct Keycloak authentication"""
    settings = get_settings()
    return settings.is_development


def is_bypass_mode() -> bool:
    """Check if in bypass/testing mode"""
    settings = get_settings()
    return settings.is_testing
