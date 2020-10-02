import random
import unittest

from Algorithms.Sort.colorSort import color_sort
from Algorithms.Sort.quickSelect import quick_select


class TestColorSort(unittest.TestCase):

    def test_color_sort(self):
        arr = [random.randint(0, 2) for _ in range(100)]
        expected = arr
        expected.sort()
        self.assertEqual(color_sort(arr), expected)


class TestQuickSelect(unittest.TestCase):

    def test_quick_select1(self):
        arr = [4, 6, 4, 3, 2, 2, 7]
        expected = 4
        target = 5
        self.assertEqual(quick_select(arr, target), expected)

    def test_quick_select2(self):
        arr = [5, 6, 4, 3, 2, 1, 7]
        for target in arr:
            self.assertEqual(quick_select(arr, target), target)

