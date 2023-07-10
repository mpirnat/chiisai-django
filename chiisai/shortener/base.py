"""
Convert to base62 (or whatever)
"""

base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def base_encode(integer: int, alphabet: str = base62) -> str:
    """
    Encode a base10 integer as a Base X string.
    """
    result: list[str] = []
    base = len(alphabet)

    while integer >= base:
        result.append(alphabet[integer % base])
        # Use //= instead of /= to keep everything ints
        integer //= base

    result.append(alphabet[integer])
    result.reverse()
    return "".join(result)


def base_decode(string_: str, alphabet: str = base62) -> int:
    """
    Decode a Base X string into a base10 integer.
    """
    base = len(alphabet)
    length = len(string_)
    integer = 0

    for i, char in enumerate(string_):
        power = length - (i + 1)
        integer += alphabet.index(char) * (base**power)

    return integer


def bytestring_to_integer(bytestring: bytes) -> int:
    """
    Convert a bytestring into its equivalent base10 integer.
    """
    integer = 0
    for i, byte in enumerate(bytestring):
        integer += byte << (8 * i)
    return integer


def integer_to_bytestring(integer: int) -> bytes:
    """
    Convert an integer into its equivalent bytestring.
    """
    if integer == 0:
        return b""

    bytes_ = []
    while integer > 0:
        bytes_.append(bchr(integer - ((integer >> 8) << 8)))
        integer >>= 8

    return b"".join(bytes_)


def bchr(value: int) -> bytes:
    """
    Like chr, but for bytes.
    """
    return bytes([int(value)])
