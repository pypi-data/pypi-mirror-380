import jwt
import uuid
import warnings

from calendar import timegm
from datetime import datetime, timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.request import Request
from typing import Any, Dict, Optional

from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings


def jwt_get_secret_key(payload: Optional[Dict[str, Any]] = None) -> str:
    """
    For enhanced security you may want to use a secret key based on user.

    This way you have an option to logout only this user if:
        - token is compromised
        - password is changed
        - etc.
    """
    if api_settings.JWT_GET_USER_SECRET_KEY:
        User = get_user_model()  # noqa: N806
        user = User.objects.get(pk=payload.get("user_id"))
        key = str(api_settings.JWT_GET_USER_SECRET_KEY(user))
        return key
    return api_settings.JWT_SECRET_KEY


def jwt_payload_handler(user: User) -> Dict[str, Any]:
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        "The following fields will be removed in the future: `email` and `user_id`. ",
        DeprecationWarning,
    )

    exp_datetime = datetime.now(timezone.utc) + (api_settings.JWT_EXPIRATION_DELTA)
    payload = {
        "user_id": user.pk,
        "username": username,
        "exp": timegm(exp_datetime.utctimetuple()),
    }
    if hasattr(user, "email"):
        payload["email"] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload["user_id"] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload["orig_iat"] = timegm(datetime.now(timezone.utc).utctimetuple())

    if api_settings.JWT_AUDIENCE is not None:
        payload["aud"] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload["iss"] = api_settings.JWT_ISSUER

    return payload


def jwt_get_user_id_from_payload_handler(payload: Dict[str, Any]) -> Any:
    """
    Override this function if user_id is formatted differently in payload
    """
    warnings.warn(
        "The following will be removed in the future. "
        "Use `JWT_PAYLOAD_GET_USERNAME_HANDLER` instead.",
        DeprecationWarning,
    )

    return payload.get("user_id")


def jwt_get_username_from_payload_handler(payload: Dict[str, Any]) -> str:
    """
    Override this function if username is formatted differently in payload
    """
    return payload.get("username")


def jwt_encode_handler(payload: Dict[str, Any]) -> bytes:
    key = api_settings.JWT_PRIVATE_KEY or jwt_get_secret_key(payload)
    return jwt.encode(payload, key, api_settings.JWT_ALGORITHM)


def jwt_decode_handler(token: str) -> Any:
    options = {
        "verify_exp": api_settings.JWT_VERIFY_EXPIRATION,
    }
    # get user from token, BEFORE verification, to get user secret key
    unverified_payload = jwt.decode(
        jwt=token,
        options={"verify_signature": False},
        algorithms=[api_settings.JWT_ALGORITHM],
    )
    secret_key = jwt_get_secret_key(unverified_payload)
    decoded = jwt.decode(
        token,
        api_settings.JWT_PUBLIC_KEY or secret_key,
        algorithms=[api_settings.JWT_ALGORITHM],
        options=options,
        leeway=api_settings.JWT_LEEWAY,
        audience=api_settings.JWT_AUDIENCE,
        issuer=api_settings.JWT_ISSUER,
    )
    # Convert datetime objects back to timestamps for backward compatibility
    if isinstance(decoded.get("exp"), datetime):
        decoded["exp"] = timegm(decoded["exp"].utctimetuple())
    if isinstance(decoded.get("iat"), datetime):
        decoded["iat"] = timegm(decoded["iat"].utctimetuple())
    if isinstance(decoded.get("nbf"), datetime):
        decoded["nbf"] = timegm(decoded["nbf"].utctimetuple())
    return decoded


def jwt_response_payload_handler(
    token: str, user: Optional[User] = None, request: Optional[Request] = None
):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }

    """
    return {"token": token}
