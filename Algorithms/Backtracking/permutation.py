from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # generate a barket
        basket = {}
        self.result = []
        for c in nums:
            if c in basket:
                basket[c] += 1
            else:
                basket[c] = 1

        def rec(basket, ans):
            if len(ans) == len(nums):
                print(ans)
                print('found')
                self.result.append(ans[:])
                print(self.result, 'result')
            else:
                for n in basket:
                    print(basket, n, ans)
                    if basket[n] > 0:
                        basket[n] -= 1
                        ans.append(n)
                        rec(basket, ans)
                        basket[n] += 1
                        ans.pop()

        if len(nums) <= 1:
            return [nums]
        else:
            rec(basket, [])
            print(self.result)
            return self.result

nums = [1,2]

result = Solution().permuteUnique(nums)

print(result)



