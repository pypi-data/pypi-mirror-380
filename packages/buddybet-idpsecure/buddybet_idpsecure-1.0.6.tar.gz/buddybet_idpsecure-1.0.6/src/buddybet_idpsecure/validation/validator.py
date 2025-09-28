from jose import jwt, ExpiredSignatureError
from jose.exceptions import JWTClaimsError, JWTError
from datetime import datetime, timezone
from buddybet_idpsecure.core.environment_config import AppConfig
from .exceptions import *
from buddybet_idpsecure.core.idp_constants import IdpConstants
from buddybet_logmon_common.logger import get_logger

from buddybet_idpsecure.model.user_claims import UserClaims
from .jwks import JWKSCache


class TokenValidator:
    logger = get_logger()

    def __init__(self, config: AppConfig):
        self.env_var = config.idp_lib_env
        self.jwksCacheObj = JWKSCache(config)

    def validate_token(self, token: str):

        if not self.jwksCacheObj:
            self.logger.error("Validator not initialized. Call init_validator()", exc_info=True)
            raise ValidatorNotInitialized()

        headers = jwt.get_unverified_header(token)
        kid = headers.get("kid")
        keys = self.jwksCacheObj.get_keys_idp()

        if kid not in keys:
            self.logger.error("Invalid KID in token header.", exc_info=True)
            raise InvalidSignature()

        key = keys[kid]
        try:
            claims_dict = jwt.decode(
                token,
                key,
                algorithms=[IdpConstants.ALGORITHM],
                audience=self.env_var.expected_audience,
                issuer=self.env_var.issuer
            )
        except ExpiredSignatureError:
            self.logger.error("Token expired.", exc_info=True)
            raise ExpiredToken()
        except JWTClaimsError as e:
            self.logger.error(f"Invalid claims:", exc_info=True)
            raise InvalidClaims()
        except JWTError as e:
            self.logger.error(f"Invalid token:", exc_info=True)
            raise InvalidToken()

        now = datetime.now(timezone.utc).timestamp()
        if "exp" in claims_dict and claims_dict["exp"] < now:
            self.logger.error(f"Token expired", exc_info=True)
            raise ExpiredToken()
        if "nbf" in claims_dict and claims_dict["nbf"] > now:
            self.logger.error(f"Token not valid yet", exc_info=True)
            raise InvalidNotBefore()

        if claims_dict.get("scope"):
            scopes = claims_dict.get("scope")
            scopes_list = scopes.split()
        else:
            scopes_list = []

        claims_dict["scope"] = scopes_list
        claims_dict["token"] = token
        return UserClaims(**claims_dict)
