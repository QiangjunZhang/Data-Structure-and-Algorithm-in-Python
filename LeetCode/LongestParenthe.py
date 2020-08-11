class Solution0:
    def longestValidParentheses(self, s: str) -> int:

        self.L = 0
        memo = {}
        memo[0] = 0
        def dp(i):
            if i < 0:
                return 0
            if i not in memo:
                if (s[i-1], s[i]) == ('(', ')'):
                    memo[i] = dp(i-2) + 2
                    self.L = max(self.L, memo[i])
                elif (s[i-1], s[i]) == (')', ')'):
                    prefix = dp(i-1)
                    if i - prefix - 1 >=0 and s[i - prefix - 1] == '(':
                        memo[i] = prefix + dp(i - prefix - 2) + 2
                        self.L = max(self.L, memo[i])
                    else:
                        memo[i] = 0
                else:
                    memo[i] = 0
            return memo[i]
        for i in range(len(s)-1, 0, -1):
            dp(i)
        return self.L

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        self.L = 0
        left_L = 0
        right_L = 0
        left_R = 0
        right_R = 0

        for i in range(len(s)):
            if s[i] == '(':
                left_L += 1
            elif s[i] == ')':
                right_L +=1

            if s[len(s)-1-i] == '(':
                left_R += 1
            elif s[len(s)-1-i] == ')':
                right_R +=1

            if left_L == right_L:
                self.L = max(self.L, 2*right_L)
            if left_R == right_R:
                self.L = max(self.L, 2 * right_R)
            if left_L < right_L:
                left_L = 0
                right_L = 0
            if left_R > right_R:
                left_R = 0
                right_R = 0
        return self.L

s = "(()"

x = Solution()
result = x.longestValidParentheses(s)

print(result)