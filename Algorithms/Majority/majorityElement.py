def find_majority(nums):

    count = 0
    for idx in range(len(nums)):
        if count == 0:
            candidate = idx
            count = 1
        elif nums[candidate] == nums[idx]:
            count += 1
        else:
            count -= 1

    check = 0
    for num in nums:
        if num == nums[candidate]:
            check += 1

    if check > len(nums) // 2:
        return candidate
    else:
        return -1