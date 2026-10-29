
from file_validator import is_valid_file_size

def test_valid_file_size():
    result = is_valid_file_size(5,10)
    assert result is True



def test_file_larger_than_max():
    result = is_valid_file_size(15,10)
    assert result is False


def test_file_same_size_max():
    result = is_valid_file_size(10,10)
    assert result is True


def test_zero_size_file():
    result = is_valid_file_size(0,10)
    assert result is False

def test_negative_sized_file():
    result = is_valid_file_size(-3, 10)
    assert result is False

