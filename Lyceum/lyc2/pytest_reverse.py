import pytest
# from reverse import reverse
from yandex_testing_lesson import reverse


def test_empty():
    assert reverse('') == ''
    assert reverse('a') == 'a'
    assert reverse('abcba') == 'abcba'
    assert reverse('abc') == 'cba'


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)
    with pytest.raises(TypeError):
        reverse([1, 1])

