from typing import List


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        # calculate the target sum of subset
        target, rem = divmod(sum(nums), k)
        if rem: return False                          # return false if target sum is not integer

        def search(groups):
            if not nums: return True                  # Goal base case: all nums are added to subsets
            v = nums.pop()                            # Make the 1st change: remove and record the last element in nums
            for i, group in enumerate(groups):        # Choice: make a decision, select an basket to put this element
                if group + v <= target:               # Constraints:
                    groups[i] += v                    # Make the 2nd change: add the element to the basket
                    if search(groups): return True    # recursive remaining groups from remaining elements
                    groups[i] -= v                    # undo the 2nd change: remove the element from the basket
                if not group: break                   # if all elements are bigger than target, break and return false
            nums.append(v)                            # undo the 1st change: put back the removed element.
            return False                              # the path is failed, return False

        nums.sort()                                 # sort the nums so the path finding is much faster.
        if nums[-1] > target: return False            # if the maximum element equals the target, so make the first basket
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)


x = Solution()

nums = [10,10,10,7,7,7,7,7,7,6,6,6]
# nums = [4,3,2,3,5,2,1]

# nums.sort(reverse=1)
print(nums)
k = 3
result = x.canPartitionKSubsets(nums, k)
print(result)