import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("привет", "Привет"),
    ("14 сентября 2025", "14 сентября 2025")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    (" ", " "),
    ("!test", "!test")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("    python", "python"),
    ("    14 сентября 2025", "14 сентября 2025"),
    ("test", "test")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("   ", ""),
    ("test   ", "test   "),
    ("  test  ", "test  ")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("hello world", " ", True),
    ("123456", "3", True),
    ("тест", "т", True),
    ("multiple words", "multiple", True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    (" ", "a", False),
    ("hello", "H", False),
    ("test", "", True),
    ("python", "java", False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("banana", "a", "bnn"),
    ("hello world", " ", "helloworld"),
    ("123-456-789", "-", "123456789"),
    ("aabbcc", "b", "aacc")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),
    (" ", "a", " "),
    ("hello", "x", "hello"),
    ("test", "", "test"),
    ("   ", " ", ""),
    ("abc", "abc", "")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
