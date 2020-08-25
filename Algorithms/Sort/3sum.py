class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        result = []
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
            else:
                for ans in self.twoSum(nums[i+1:], -nums[i]):
                    result.append([nums[i]] + ans)
                i += 1
        return result
        
    
    def twoSum(self, nums, target):
        ans = []
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                ans.append([nums[left],nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
        return ans


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i, num in enumerate(nums[:-2]):
            diff = self.twoSumClosest(nums[i+1:], target - num)
            if abs(diff) < abs(ans): 
                ans = diff
        return target - ans

    def twoSumClosest(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = float('inf')
        while left < right:
            diff = target - nums[left] - nums[right] 
            if abs(diff) < abs(ans): 
                ans = diff
            if diff < 0:
                right -= 1
            elif diff > 0:
                left += 1
            else:
                return 0
        return ans

                
                
        
        

        
        
        
        
        