from typing import List


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        ans = [0] * len(candidates)
        candidates.sort()

        def dp(i, res):
            if res == 0:
                match = []
                for i, count in enumerate(ans):
                    if count:
                        match = match + [candidates[i]]*count
                result.append(match)
                return True
            elif i > len(candidates) - 1 and res != 0:
                return False
            a = 0
            while a <= res / candidates[i]:
                ans[i] = a
                dp(i + 1, res - a * candidates[i])
                a += 1
        dp(0, target)
        return result


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # could be optimised using dynamic programming.
        memo = {}
        def dp(i, res):
            if (i, res) not in memo:
                memo[i, res] = []
                if res == 0:
                    memo[i, res] = []
                elif res < 0:
                    memo[i, res] = []
                else:
                    for j in range(i, len(candidates)):
                        if candidates[j] > res:
                            break
                        elif candidates[j] == res:
                            memo[i, res].append([candidates[j]])
                        elif dp(j+1, res - candidates[j]):
                            for l in memo[j+1, res - candidates[j]]:
                                memo[i, res].append([candidates[j]] + l)
            return memo[i, res]
        dp(0, target)
        return memo[0, target]

candidates = [2,3,5,7]
target = 7

x = Solution()

result = x.combinationSum(candidates, target)
print(result)
# print([1] + [2])
