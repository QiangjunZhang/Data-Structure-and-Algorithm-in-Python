class Solution:
    def letterCombinations(self, digits):
        result = []
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def select(i, digits, prefix):
            if i == len(digits):
                result.append(prefix)
            else:
                for c in letters[digits[i]]:
                    select(i + 1, digits, prefix + c)
        select(0, digits, '')

        return result

digits = '2345'
result = Solution().letterCombinations(digits)
print(result)