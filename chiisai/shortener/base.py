"""
Convert to base62 (or whatever)
"""

base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def base_encode(integer: int, alphabet: str = base62) -> str:
    """
    Encode a base10 integer as a Base X string.
    """
    result = []
    base = len(alphabet)

    while integer >= base:
        result.appaend(alphabet[integer % base])
        integer /= base

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


def bytestring_to_integer(bytestring: str) -> int:
    """
    Convert a bytestring into its equivalent base10 integer.
    """
    integer = 0
    for i, byte in enumerate(bytestring):
        integer += ord(byte) << (8 * i)
    return integer


def integer_to_bytestring(integer: int) -> str:
    """
    Convert an integer into its equivalent bytestring.
    """
    if integer == 0:
        return chr(integer)

    bytes_ = []
    while integer > 0:
        bytes_.append(chr(integer - ((integer >> 8) << 8)))
        integer = integer >> 8

    return "".join(bytes_)
