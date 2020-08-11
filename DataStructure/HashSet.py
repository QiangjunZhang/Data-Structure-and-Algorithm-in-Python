class HashSet:
    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] != None:
            if items[idx] == item:
                # item already in set
                return False

            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

        return True

    def __remove(item, items):
        idx = hash(item) % len(items)

        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True

            idx = (idx + 1) % len(items)

        return False

    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, newList)

        return newList

    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.numItems = 0

        for item in contents:
            self.add(item)

    def __str__(self):
        pass

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]

                # Following are the mutator set methods

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None] * 2 * len(self.items))

    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None] * int(len(self.items) / 2))
        else:
            raise KeyError("Item not in HashSet")

    def discard(self, item):
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    def update(self, other):
        pass

    def intersection_update(self, other):
        pass

    def difference_update(self, other):
        for item in other:
            self.discard(item)

    def symmetric_difference_update(self, other):
        pass

    # Following are the accessor methods for the HashSet  
    def __len__(self):
        pass

    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False

    # One extra method for use with the HashMap class. This method is not needed in the 
    # HashSet implementation, but it is used by the HashMap implementation. 
    def __getitem__(self, item):
        pass

    def not__contains__(self, item):
        pass

    def isdisjoint(self, other):
        pass

    def issubset(self, other):
        pass

    def issuperset(self, other):
        pass

    def union(self, other):
        pass

    def intersection(self, other):
        pass

    # done
    def difference(self, other):
        pass

    def symmetric_difference(self, other):
        pass

    def copy(self):
        pass

    # Operator Definitions
    def __or__(self, other):
        pass

    def __and__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __ior__(self, other):
        pass

    def __iand__(self, other):
        pass

    def __ixor(self, other):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass


def main():
    s = HashSet(list(range(100)))

    t = HashSet(list(range(10, 20)))

    u = HashSet(list(range(10, 20)))

    if len(t) == len(u) and len(t) == 10:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    s.intersection_update(t)

    if len(s) == 10:
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    s = HashSet(list(range(100)))

    t.update(s)

    if len(s) == len(t):
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    t.clear()
    t.update(u)


if __name__ == "__main__":
    main()
