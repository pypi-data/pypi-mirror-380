# -*- coding: utf-8 -*-

"""
JWT token wrapper module for authentication
operations.
"""

from __future__ import annotations

import json
from contextlib import suppress
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Union, Optional

from jwt import ExpiredSignatureError
from jwt import InvalidTokenError
from jwt import PyJWK
from jwt import PyJWTError
from jwt import decode, encode, decode_complete
from jwt.algorithms import requires_cryptography
from .algorithm import ALGORITHM

with suppress(ImportError):
    from cryptography.hazmat.primitives.asymmetric.ec import (
        EllipticCurvePrivateKey,
        EllipticCurvePublicKey,
    )

    from cryptography.hazmat.primitives.asymmetric.ed448 import (
        Ed448PrivateKey,
        Ed448PublicKey,
    )

    from cryptography.hazmat.primitives.asymmetric.ed25519 import (
        Ed25519PrivateKey,
        Ed25519PublicKey,
    )

    from cryptography.hazmat.primitives.asymmetric.rsa import (
        RSAPrivateKey,
        RSAPublicKey,
    )


AllowedPrivateKeys = Union[
    RSAPrivateKey, EllipticCurvePrivateKey,
    Ed25519PrivateKey, Ed448PrivateKey
]

AllowedPublicKeys = Union[
    RSAPublicKey, EllipticCurvePublicKey,
    Ed25519PublicKey, Ed448PublicKey
]


class JwtToken:
    """ Wrapper around JWT tokens """

    def __init__(
        self,
        private_key: AllowedPrivateKeys | PyJWK | bytes | str,
        public_key: Optional[AllowedPublicKeys | PyJWK | str | bytes] = None,
        expire: int = 3600,
    ) -> None:
        """
        :param private_key: Secret key to create, encode and decode the tokens.
        :param expire: Seconds until the token expires.
        """

        self.private_key = private_key
        self.public_key = public_key
        self.expire = expire

    @staticmethod
    def from_auth_header(auth_header: str):
        """ It retrieves the token from the authentication headers """

        data = auth_header.split()
        if len(data) != 2 or data[0].lower() != "bearer":
            raise JwtException("Bad format in Authorization header. Must be: Bearer <token>")

        return data[1]

    def encode(
        self,
        subject: Any = None,
        algorithm: ALGORITHM | str = ALGORITHM.HS256,
        claims: Optional[Dict[str, str]] = None,
        headers: Optional[Dict] = None,
        json_encoder: Optional[type[json.JSONEncoder]] = None,
    ) -> str:
        """
        Encode the payload as Json Web Token.
        More Info: https://pyjwt.readthedocs.io/en/stable/api.html#jwt.encode

        :param subject: Information will be place into the `sub` claim.
        :param algorithm: Algorithm to use like: HS256.

        :param claims: Other claims to add in the payload. For more information about standardized claims:
            - https://auth0.com/docs/secure/tokens/json-web-tokens/json-web-token-claims#registered-claims
            - https://www.iana.org/assignments/jwt/jwt.xhtml#claims

        :param headers: Additional JWT header fields.
        :param json_encoder: Custom JSON encoder for payload and headers.

        :return: The Json Web Token.
        """

        if not claims:
            claims = {}

        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(seconds=self.expire),
            "iat": datetime.now(timezone.utc),
            "sub": subject,
            **claims
        }

        try:
            return encode(
                payload, self.private_key, algorithm=algorithm,
                headers=headers, json_encoder=json_encoder)

        except Exception as error:
            raise JwtException(f"Error generating JWT token. Error: {error}")

    def decode(
        self,
        token: str,
        algorithms: Optional[List[ALGORITHM | str]] = None,
        options: Optional[Dict] = None,
        audience: Optional[List[str] | str] = None,
        issuer: Optional[str] = None,
        leeway: timedelta | float = 0,
        full_decode: bool = False,
    ) -> Dict:
        """
        It decodes and verifies the JWT token signature and return the token claims.
        More Info: https://pyjwt.readthedocs.io/en/stable/api.html#jwt.decode

        :param token: Token to decode.
        :param algorithms: Algorithms to use like: HS256 or RS256.

        :param options: Extended decoding and validation options.
          - verify_signature=True verify the JWT cryptographic signature.
          - require=[] claims that must be present. Example: require=["exp", "iat", "nbf"].
          - verify_aud=verify_signature check that aud (audience) claim matches audience
          - verify_iss=verify_signature check that iss (issuer) claim matches issuer
          - verify_exp=verify_signature check that exp (expiration) claim value is in the future
          - verify_iat=verify_signature check that iat (issued at) claim value is an integer
          - verify_nbf=verify_signature check that nbf (not before) claim value is in the past
          - strict_aud=False check that the aud claim is a single value (not a list), and matches audience exactly

        :param audience: The value for verify_aud check.
        :param issuer: The value for verify_iss check.
        :param leeway: A time margin in seconds for the expiration check
        :param full_decode: If True, full_decode will be performed.

        :return: The JWT claims or full payload.

            Example::

                # If full_decode.

                {
                    'payload': {
                        'exp': ...,
                        'iat': ...,
                        'sub': '...',
                        'iss': '...'
                    },
                    'header': {
                        'alg': 'HS256',
                        'typ': 'JWT'
                    },
                    'signature': b'...'
                }

                # Else.

                {
                    'exp': ...,
                    'iat': ...,
                    'sub': '...'
                }
        """

        if algorithms is None:
            algorithms = [ALGORITHM.HS256]

        fcn = decode
        if full_decode:
            fcn = decode_complete  # type: ignore[assignment]

        key = self.public_key \
            if any(map(lambda x: x in algorithms, requires_cryptography)) \
            else self.private_key

        try:
            return fcn(
                token,
                key,  # type: ignore[arg-type]
                algorithms=algorithms,
                options=options,
                audience=audience,
                issuer=issuer,
                leeway=leeway,
            )

        except ExpiredSignatureError as error:
            raise JwtException("Signature expired.") from error

        except InvalidTokenError as error:
            raise JwtException("Invalid token.") from error


class JwtException(PyJWTError):
    """ JWT Exception """
