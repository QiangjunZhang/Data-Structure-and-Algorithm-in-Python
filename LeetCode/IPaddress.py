from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        memo = {}

        def dp(i, j, k):
            if k == 0:
                if i > j:
                    memo[i, j, k] = [[]]
                    return True
                else:
                    return False
            else:
                if (i, j, k) not in memo:
                    if j - i + 1 > 3 * k or j - i + 1 < k:
                        return False
                    memo[i, j, k] = []
                    if j == i:
                        memo[i, j, k].append([s[i]])
                    # keep one element
                    if j > i and dp(i + 1, j, k - 1):
                        print('keep one element', i, j, k)
                        print(i + 1, j, k - 1, memo[i + 1, j, k - 1])
                        for c in memo[i + 1, j, k - 1]:
                            print(c)
                            memo[i, j, k].append([s[i]] + c)
                    # keep two element
                    if j >= i + 1 and dp(i + 2, j, k - 1):
                        print('keep two element', i, j, k)
                        print(i + 2, j, k - 1, memo[i + 2, j, k - 1])
                        for c in memo[i + 2, j, k - 1]:
                            memo[i, j, k].append([s[i:i + 2]] + c)
                    # keep three element
                    if j >= i + 2 and int(s[i:i + 3]) < 256 and dp(i + 3, j, k - 1):
                        print('keep three element', i, j, k)
                        print(i + 3, j, k - 1, memo[i + 3, j, k - 1])
                        for c in memo[i + 3, j, k - 1]:
                            memo[i, j, k].append([s[i:i + 3]] + c)
                    print(i, j, k, 'final', memo[i, j, k])
                if memo[i, j, k]:
                    return True
                else:
                    return False

        dp(0, len(s) - 1, 4)
        result = []
        print(memo)
        for c in memo[0, len(s) - 1, 4]:
            result.append('.'.join(c))
        return result

s = '25593'

result = Solution().restoreIpAddresses(s)

print(result)















