class Solution(object):
    def first(self,nums, target):
        l = -1
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                high = mid-1
                l = mid
            elif nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
        return l


    def last(self, nums, target):
        h = -1
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                low = mid+1
                h = mid
            elif nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
        return h
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.first(nums, target), self.last(nums,target)]

nums = [1, 2, 3 ,4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9, 10]

target = 5

x = Solution()

x.first(nums, target)