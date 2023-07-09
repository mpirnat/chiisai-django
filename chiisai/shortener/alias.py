"""
Core logic for generating and using aliases.
"""

from hashlib import md5
from typing import Optional

from .base import base_encode, bytestring_to_integer

# TODO: move to settings?
ALIAS_LENGTH = 4


class UncleanAlias(ValueError):
    pass


def make_alias(
    url: str, alias: Optional[str] = None, length: int = ALIAS_LENGTH
) -> str:
    """
    Generate an alias for a URL.
    """
    if alias and not is_clean(alias):
        raise UncleanAlias(f"alias '{alias}' is not clean")

    attempt = 0
    attempt_url = url

    while not alias:
        hashed = make_hash(attempt_url)

        if is_clean(hashed):
            alias = hashed[:length]

        else:
            attempt += 1
            attempt_url = f"{url}#{attempt}"

    return alias


def make_hash(value: str) -> str:
    """
    Make a URL-friendly md5 hash of a value.
    """
    hasher = md5()
    hasher.update(value)

    # Get the hashed value, being careful to strip out characters that are not
    # URL-safe
    hash_ = base_encode(bytestring_to_integer(hasher.digest()))

    return hash_


RESERVED_WORDS = ("admin",)
# TODO: read from a separate bad words file
BAD_WORDS = []


def is_clean(value: str) -> bool:
    """
    Is the value devoid of "unsavory" language?
    """
    value = value.lower()

    for word in RESERVED_WORDS:
        if word in value:
            return False

    for word in BAD_WORDS:
        if word in value:
            return False

    return True