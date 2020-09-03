class PyList:
    def __init__(self, contents=[], size = 4):
        self.items = [None] * size
        self.size = 0
        for item in contents:
            self.append(item)

    def __make_room(self):
        new_list = [None] * self.size * 2
        for i in range(self.size):
            new_list[i] = self.items[i]
        self.items = new_list

    def append(self, item):
        if self.size == len(self.items):
            self.__make_room()
        self.items[self.size] = item
        self.size += 1

    def len(self):
        return self.size

    def get(self, index):
        if 0 <= index < self.size:
            return self.items[index]
        else:
            return 'Key Error'

