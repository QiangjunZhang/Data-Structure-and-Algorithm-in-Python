class JumpGame:
    def jump(self, nums):
        """
        keep a monotonic jump range
        """
        stack = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                stack[i] = 1
            elif nums[i] < 1:
                stack[i] = float('inf')
            else:
                stack[i] = stack[i + nums[i]] + 1
            while stack[i] < stack[i + 1] and i < len(nums) - 1:
                stack[i + 1] = stack[i]
                i += 1
        return stack[0]
