import time

from typing import cast

import jwt

from django.contrib.auth.models import AnonymousUser
from requests import HTTPError
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request

from jsm_user_services import settings
from jsm_user_services.drf.exceptions import ExpiredToken
from jsm_user_services.drf.exceptions import InvalidToken
from jsm_user_services.drf.exceptions import NotAuthenticated
from jsm_user_services.services.user import current_jwt_token
from jsm_user_services.services.user import get_user_data_from_server
from jsm_user_services.support.auth_jwt import decode_jwt_token
from jsm_user_services.typings import LvUserData


class BaseJsmJwtAuthentication(BaseAuthentication):
    """
    Base class for JWT authentication classes.

    Provides a method to retrieve user data from the request or from the user microservice.
    """

    APPEND_USER_DATA = settings.JSM_USER_SERVICES_DRF_APPEND_USER_DATA
    USER_DATA_ATTR_NAME = settings.JSM_USER_SERVICES_DRF_REQUEST_USER_DATA_ATTR_NAME

    @classmethod
    def _retrieve_user_data(cls, request: Request) -> LvUserData:
        """
        Tries to retrieve a valid user_data from the request.
        If not found, it requests it from the user microservice.
        """
        try:
            user_data = getattr(request, cls.USER_DATA_ATTR_NAME)
        except AttributeError:
            user_data_from_server = get_user_data_from_server()
            user_data = user_data_from_server.get("data", {})

        return user_data

    def authenticate(self, request: Request) -> tuple[AnonymousUser, str] | None:
        raise NotImplementedError("Subclasses must implement the authenticate method.")


class OauthJWTAuthentication(BaseJsmJwtAuthentication):
    """
    Authentication class for OAuth JWT tokens.
    Should be used in DRF views that need to use Auth0 tokens.
    """

    def authenticate(self, request: Request) -> tuple[AnonymousUser, str] | None:
        token = current_jwt_token()
        if token is None:
            raise NotAuthenticated()

        try:
            payload = decode_jwt_token(token)
            current_timestamp = int(time.time())
            is_token_expired = "exp" in payload and current_timestamp > payload["exp"]
            is_sub_claim_in_payload = "sub" in payload
            if not is_token_expired and is_sub_claim_in_payload:
                return (AnonymousUser(), token)
            else:
                raise InvalidToken()
        except jwt.DecodeError:
            raise InvalidToken()


class LvJWTAuthentication(BaseJsmJwtAuthentication):
    """
    Authentication class for LV JWT tokens.
    Should be used in DRF views that need to use LV tokens.
    """

    def authenticate(self, request: Request) -> tuple[AnonymousUser, str] | None:
        """
        Authenticates the request using the LV JWT token.

        This authentication logic will:
            1. Decode the JWT token.
            2. Set the decoded payload in the request as 'jwt_payload'.
            3. Retrieve user data from the user microservice/request and optionally append it to the request.
            4. Return an AnonymousUser and the token if authentication is successful.
        """
        token = current_jwt_token()
        if token is None:
            raise NotAuthenticated()

        try:
            payload = decode_jwt_token(token)
        except jwt.DecodeError as e:
            raise InvalidToken() from e
        except jwt.ExpiredSignatureError as e:
            raise ExpiredToken() from e

        # Set the payload in the request
        setattr(request, "jwt_payload", payload)

        try:
            user_data = cast(LvUserData, self._retrieve_user_data(request))
            if self.APPEND_USER_DATA:
                setattr(request, self.USER_DATA_ATTR_NAME, user_data)
        except (HTTPError, KeyError) as retrieve_user_data_error:
            raise InvalidToken() from retrieve_user_data_error

        return AnonymousUser(), token
