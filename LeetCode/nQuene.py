from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = [['.']*n for i in range(n)]
        for i in range(n):
            solution[i][i] = 'Q'
        origin = []
        for i in range(n):
            origin.append(''.join(solution[i]))
        cols = set([i for i in range(n)])
        used_cols = set()
        occupied_45 = set()
        occupied_135 = set()
        ans = []
        self.result = []
        def chose(row):
            if row == n:
                self.result.append(ans[:])
            else:
                l = len(cols)
                for col in cols:
                    if (row-col) not in occupied_45 and (row + col) not in occupied_135 and col not in used_cols:
                        ans.append(origin[col])
                        occupied_45.add(row-col)
                        occupied_135.add(row+col)
                        used_cols.add(col)
                        chose(row+1)
                        used_cols.remove(col)
                        occupied_45.remove(row-col)
                        occupied_135.remove(row+col)
                        ans.pop()
        chose(0)
        return self.result


result = Solution().solveNQueens(4)
print(result)