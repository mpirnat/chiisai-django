from shortener.base import (
    base_decode,
    base_encode,
    bytestring_to_integer,
    integer_to_bytestring,
)


class TestBase62Conversions:
    """
    Test that base_encode and base_decode behave as expected and are each
    other's inverse.
    """

    EXPECTED_INTEGER = 11382187
    EXPECTED_BASE62_STRING = "ll1f"

    def test_base_encode__base62(self):
        base62_string = base_encode(self.EXPECTED_INTEGER)
        assert base62_string == self.EXPECTED_BASE62_STRING

    def test_base_decode__base62(self):
        integer = base_decode(self.EXPECTED_BASE62_STRING)
        assert integer == self.EXPECTED_INTEGER


class TestBytestringIntegerConversions:
    """
    Test that bytestring_to_integer and integer_to_bytestring behave as
    exepected and are each other's inverse.
    """

    EXPECTED_BYTESTRING = b"abcd1234"
    EXPECTED_INTEGER = 3761405301503517281

    def test_bytestring_to_integer(self):
        integer = bytestring_to_integer(self.EXPECTED_BYTESTRING)
        assert integer == self.EXPECTED_INTEGER

    def test_integer_to_bytestring(self):
        bytestring = integer_to_bytestring(self.EXPECTED_INTEGER)
        assert bytestring == self.EXPECTED_BYTESTRING

    def test_integer_to_bytestring__zero(self):
        bytestring = integer_to_bytestring(0)
        assert bytestring == b""
