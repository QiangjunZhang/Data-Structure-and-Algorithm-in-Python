def max_sub_array(nums):
    global_max = float('-inf')
    local_max = 0

    for num in nums:
        local_max = max(num, local_max + num)
        global_max = max(global_max, local_max)

    return global_max


class MaxSubArray:
    pass