class Solution():
    def solve(self, nums):
        self.ans = 0
        maxid = [(nums[0], 0)]
        for i, c in enumerate(nums):
            far = i + c
            if far > maxid[-1][0]:
                maxid.append((far, i))
        pivot = len(nums) - 1

        i = len(maxid) - 1
        while pivot > 0:
            all_pos = []
            while maxid[i][0] >= pivot and i >=0:
                all_pos.append(maxid[i][1])
                i -= 1
            pivot = min(all_pos)
            self.ans += 1
        return self.ans



nums = [1,1,1,1,1]

result = Solution().solve(nums)

basket = {2:1, 3: 1}
for i in basket:
    basket[i] = 0
print(basket)

print(result)
