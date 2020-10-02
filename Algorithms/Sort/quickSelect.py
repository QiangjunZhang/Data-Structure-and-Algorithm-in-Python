def quick_select(arr, target):
    target = target - 1   # convert to 0 indexed
    curr = helper(0, len(arr) - 1, arr, target)
    while curr != target:
        if curr < target:
            curr = helper(curr+1, len(arr) - 1, arr, target)
        else:
            curr = helper(0, curr - 1, arr, target)
    return arr[curr]


def helper(left, right, arr, target):
    pivot = arr[right]
    curr = left

    while curr < right:
        if arr[curr] > pivot:
            curr += 1
        else:
            arr[curr], arr[left] = arr[left], arr[curr]
            left += 1
            curr += 1

    arr[left], arr[right] = arr[right], arr[left]

    return left
