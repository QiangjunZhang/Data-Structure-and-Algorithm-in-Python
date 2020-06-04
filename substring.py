class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = []
        n = 0
        while n < len(s):
            sub = {s[n]: n }
            n +=1
            for k in range(n , len(s)):
                if s[k] in sub:
                    n = sub[s[k]]+1
                    break
                else:
                    sub.update({s[k]:k})
            result.append(len(sub))

        return max(result)

def main():
    x = Solution()
    s = "pwssslidwksdew"
    print(x.lengthOfLongestSubstring(s))


def test():
    x = {'x': 1}
    x.update({'testy': 2})
    y = x['testy']
    print(y)


if __name__ == '__main__':
    main()
    # test()






