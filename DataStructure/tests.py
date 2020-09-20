import unittest

from DataStructure.OrderedDict import LRUCache
from DataStructure.pylist import PyList
from DataStructure.hashset import HashSet
from DataStructure.trie import Trie

class PyListMethods(unittest.TestCase):
    def test_append(self):
        list1 = PyList([1,2,3])
        list1.append(4)
        self.assertEqual(list1.get(0), 1)
        self.assertEqual(list1.get(1), 2)
        self.assertEqual(list1.get(2), 3)
        self.assertEqual(list1.get(3), 4)
        self.assertEqual(list1.get(4), 'Key Error')
        list1.append(5)
        self.assertEqual(list1.get(4), 5)

    def test_len(self):
        list1 = PyList([1, 2, 3])
        list1.append(4)
        self.assertEqual(list1.len(), 4)
        list1.append(5)
        self.assertEqual(list1.len(), 5)
        for _ in range(5):
            list1.append(5)
        self.assertEqual(list1.len(), 10)


class HashSetMethods(unittest.TestCase):
    def test_add(self):
        s = HashSet()
        self.assertEqual(5 in s, False)
        s.add(5)
        self.assertEqual(5 in s, True)
        s.add(6)
        self.assertEqual(6 in s, True)
        s.add(7)
        self.assertEqual(7 in s, True)

    def test_remove(self):
        s = HashSet()
        self.assertEqual(5 in s, False)
        s.add(5)
        s.add(15)
        s.add(6)
        self.assertEqual(5 in s, True)
        self.assertEqual(6 in s, True)
        self.assertEqual(7 in s, False)
        s.remove(5)
        with self.assertRaisesRegex(KeyError, 'Item not in HashSet'):
            s.remove(7)
        self.assertEqual(5 in s, False)


class TestLRU(unittest.TestCase):
    def test_LRU(self):
        obj = LRUCache(2)
        self.assertEqual(obj.get(1), -1)
        obj.put(1, 1)
        obj.put(2, 2)
        self.assertEqual(obj.get(1), 1)
        obj.put(3, 3)
        self.assertEqual(obj.get(2), -1)
        obj.put(4, 4)
        self.assertEqual(obj.get(1), -1)
        self.assertEqual(obj.get(3), 3)
        self.assertEqual(obj.get(4), 4)
        obj.put(5, 5)
        self.assertEqual(obj.get(3), -1)
        obj.put(4, 3)
        self.assertEqual(obj.get(4), 3)


class TestTrie(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        self.assertEqual(trie.search('banana'), False)
        trie.insert('banana')
        self.assertEqual(trie.search('banana'), True)
        self.assertEqual(trie.search('bana'), False)
        self.assertEqual(trie.search('apple'), False)
        trie.insert('apple')
        self.assertEqual(trie.search('apple'), True)



if __name__ == '__main__':
    unittest.main()
