def solver(S, P, Q):
    """
    use prefix sum to get the minimum value within certain range[i,j]
    if prefix_sum[j] - prefix_sum[i-1] > 0: means it contains at lease one element in this range.
    So O(1) time
    """
    pre_sum_A = [0] * (len(S) + 1)
    pre_sum_C = [0] * (len(S) + 1)
    pre_sum_G = [0] * (len(S) + 1)

    for i, char in enumerate(S):
        i += 1
        if char == 'A':
            pre_sum_A[i] = pre_sum_A[i - 1] + 1
        else:
            pre_sum_A[i] = pre_sum_A[i - 1]
        if char == 'C':
            pre_sum_C[i] = pre_sum_C[i - 1] + 1
        else:
            pre_sum_C[i] = pre_sum_C[i - 1]
        if char == 'G':
            pre_sum_G[i] = pre_sum_G[i - 1] + 1
        else:
            pre_sum_G[i] = pre_sum_G[i - 1]

    ans = []
    for i in range(len(P)):
        left = P[i] + 1
        right = Q[i] + 1
        if pre_sum_A[right] - pre_sum_A[left - 1] > 0:
            ans.append(1)
        elif pre_sum_C[right] - pre_sum_C[left - 1] > 0:
            ans.append(2)
        elif pre_sum_G[right] - pre_sum_G[left - 1] > 0:
            ans.append(3)
        else:
            ans.append(4)
    return ans