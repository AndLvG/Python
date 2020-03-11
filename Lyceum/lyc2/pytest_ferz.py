import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_empty():
    assert is_under_queen_attack('a1', 'a1') is True
    assert is_under_queen_attack('a1', 'b3') is False


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(1, 1)
    with pytest.raises(TypeError):
        is_under_queen_attack([1, 1])