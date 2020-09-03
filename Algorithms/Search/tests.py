import unittest
from Algorithms.Search.searchRotatedSortedArray import SearchRotatedArray


class TestSearchRotatedSortedArr(unittest.TestCase):
    def test_find_min(self):
        arr = SearchRotatedArray([4,5,6,7,0,1,2,3])
        self.assertEqual(arr.find_min(), 0)

        arr = SearchRotatedArray([4, 5, 6, 7, 1, 2, 3])
        self.assertEqual(arr.find_min(), 1)

        arr = SearchRotatedArray([4, 5, 6, 2, 3])
        self.assertEqual(arr.find_min(), 2)

        arr = SearchRotatedArray([4, 4, 5, 5, 6, 2, 2, 3, 3, 4])
        self.assertEqual(arr.find_min(), 2)

        arr = SearchRotatedArray([2, 2, 2, 0, 1])
        self.assertEqual(arr.find_min(), 0)

    def test_find_target(self):
        arr = SearchRotatedArray([4,5,6,7,0,1,2,3])
        self.assertEqual(arr.find_target(6), 2)

        arr = SearchRotatedArray([4,5,6,7,0,1,2,3])
        self.assertEqual(arr.find_target(0), 4)

        arr = SearchRotatedArray([4,5,6,7,0,1,2,3])
        self.assertEqual(arr.find_target(5), 1)

        arr = SearchRotatedArray([3, 1])
        self.assertEqual(arr.find_target(1), 1)

        arr = SearchRotatedArray([3, 3, 0, 1])
        self.assertEqual(arr.find_target(1), 3)

        arr = SearchRotatedArray([3, 3, 0, 1])
        self.assertEqual(arr.find_target(3), 1)


if __name__ == '__main__':
    unittest.main()



