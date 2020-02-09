import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')
        self.assertEqual(reverse('a'), 'a')
        self.assertEqual(reverse('abcba'), 'abcba')
        self.assertEqual(reverse('abc'), 'cba')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)
        with self.assertRaises(TypeError):
            reverse([1, 1])


if __name__ == '__main__':
    unittest.main()
