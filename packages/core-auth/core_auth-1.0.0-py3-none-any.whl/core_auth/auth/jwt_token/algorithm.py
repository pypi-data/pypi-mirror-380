# -*- coding: utf-8 -*-

"""
JWT algorithm enumeration for cryptographic
signing operations.
"""

try:
    from enum import StrEnum
except ImportError:
    from core_mixins.compatibility import StrEnum  # type: ignore[import-untyped, no-redef]


class ALGORITHM(StrEnum):
    """
    Supported  algorithms for cryptographic signing.
    More info: https://pyjwt.readthedocs.io/en/stable/algorithms.html
    """

    HS256 = "HS256"     # HMAC using SHA-256 hash algorithm (default)
    HS384 = "HS384"     # HMAC using SHA-384 hash algorithm
    HS512 = "HS512"     # HS512 - HMAC using SHA-512 hash algorithm
    ES256 = "ES256"     # ECDSA signature algorithm using SHA-256 hash algorithm
    ES256K = "ES256K"   # ECDSA signature algorithm with secp256k1 curve using SHA-256 hash algorithm
    ES384 = "ES384"     # ECDSA signature algorithm using SHA-384 hash algorithm
    ES512 = "ES512"     # ECDSA signature algorithm using SHA-512 hash algorithm
    RS256 = "RS256"     # RSASSA-PKCS1-v1_5 signature algorithm using SHA-256 hash algorithm
    RS384 = "RS384"     # RSASSA-PKCS1-v1_5 signature algorithm using SHA-384 hash algorithm
    RS512 = "RS512"     # RSASSA-PKCS1-v1_5 signature algorithm using SHA-512 hash algorithm
    PS256 = "PS256"     # RSASSA-PSS signature using SHA-256 and MGF1 padding with SHA-256
    PS384 = "PS384"     # RSASSA-PSS signature using SHA-384 and MGF1 padding with SHA-384
    PS512 = "PS512"     # RSASSA-PSS signature using SHA-512 and MGF1 padding with SHA-512
    EdDSA = "EdDSA"     # Both Ed25519 signature using SHA-512 and Ed448 signature using SHA-3 are supported. Ed25519 and Ed448 provide 128-bit and 224-bit security respectively.
