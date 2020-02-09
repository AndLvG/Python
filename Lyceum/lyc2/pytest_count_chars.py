import pytest
# from reverse import reverse
from yandex_testing_lesson import count_chars


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)
    with pytest.raises(TypeError):
        count_chars([1, 1])

