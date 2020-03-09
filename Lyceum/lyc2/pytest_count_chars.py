import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    assert count_chars('aabbb') == {'a': 2, 'b': 3}


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)
    with pytest.raises(TypeError):
        count_chars([1, 1])
