def color_sort(arr):

    left = 0
    right = len(arr) - 1
    curr = 0

    while curr <= right:
        if arr[curr] == 1:
            curr += 1
        elif arr[curr] == 0:
            arr[curr], arr[left] = arr[left], arr[curr]
            left += 1
            curr += 1
        else:
            arr[curr], arr[right] = arr[right], arr[curr]
            right -= 1

    return arr
