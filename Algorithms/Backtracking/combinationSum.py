class CombinationSum:
    def __init__(self, content=[]):
        self.arr = content
        self.result = []
        self.temp = []

    def combinationSum(self, target):
        self.temp = []
        self.arr.sort()
        self.dfs(target, 0)
        return self.result

    def dfs(self, target, start):
        if target == 0:
            self.result.append(self.temp[:])
        elif target >= self.arr[0]:
            for i in range(start, len(self.arr)):
                if i > start and self.arr[i] == self.arr[i - 1]:
                    continue
                if self.arr[i] <= target:
                    self.temp.append(self.arr[i])
                    self.dfs(target - self.arr[i], i + 1)
                    self.temp.pop()
