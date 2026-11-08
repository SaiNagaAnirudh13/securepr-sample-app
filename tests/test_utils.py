from app.utils import greet, add, subtract, is_valid_name


def test_greet():
    assert greet("World") == "Hello, World!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_valid_name():
    assert is_valid_name("Sai") is True
    assert is_valid_name("A") is False
    assert is_valid_name("") is False
