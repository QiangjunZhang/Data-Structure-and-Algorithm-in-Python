from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # generate a word count dic
        if words == []:
            return []

        if words[0] == '':
            return [i for i in range(len(s) + 1)]

        k = len(words[0])

        if len(s) < len(words) * k:
            return []

        basket = {}
        self.basket_size = len(words)
        for word in words:
            if word in basket:
                basket[word] += 1
            else:
                basket[word] = 1

        self.seen = 0

        def check(i):
            if self.basket_size == 0:
                self.seen = i - (len(words) - 1)*k
                return True
            if i < len(s) and i + k <= len(s):
                pointer = s[i:i + k]
                if pointer in basket and basket[pointer] > 0:
                    basket[pointer] -= 1
                    self.basket_size -= 1
                    if check(i + k):
                        basket[pointer] += 1
                        self.basket_size += 1
                        return True
                    else:
                        basket[pointer] += 1
                        self.basket_size +=1
                        self.seen = self.seen - k
                        return False
                elif pointer in basket and basket[pointer] == 0:
                    self.seen = i + k
                    return False
                else:
                    self.seen = i + k
                    return False
            else:
                self.seen = i + k
                return False

        result = []
        for i in range(k):
            self.seen = i
            while len(s) - self.seen >= len(words) * k:
                if check(self.seen):
                    result.append(self.seen - k)

        return result

s = "barfoothefoobarman"

words = ["foo","bar"]

x = Solution()
# result = x.findSubstring(s, words)

x = 2
y = 3
print(x , y == 2 ,3)
# print(result)

