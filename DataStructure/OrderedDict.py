from collections import OrderedDict


class LRUCache:
    """
    requirements:
    1. access a certain element in O(1)
    2. add new element in O(1)
    3. delete an element in O(1)
    4. pop end in O(1)
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            first = next(iter(self.cache))
            del self.cache[first]
        self.cache[key] = value
        self.cache.move_to_end(key)
