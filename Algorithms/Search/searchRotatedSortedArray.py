class SearchRotatedArray:
    def __init__(self, content):
        self.arr = content

    def find_min(self):
        left = 0
        right = len(self.arr) - 1
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] < self.arr[right]:
                ans = min(ans, self.arr[mid])
                right = mid - 1
            elif self.arr[left] < self.arr[mid]:
                ans = min(ans, self.arr[left])
                left = mid + 1
            else:
                ans = min(self.arr[left], ans)
                left += 1
        return ans

    def find_target(self, target):
        left = 0
        right = len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == target:
                return mid
            if self.arr[mid] < self.arr[right]:
                if self.arr[mid] < target <= self.arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif self.arr[left] < self.arr[mid]:
                if self.arr[left] <= target < self.arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if self.arr[left] != target:
                    left += 1
                else:
                    return left
        return -1




