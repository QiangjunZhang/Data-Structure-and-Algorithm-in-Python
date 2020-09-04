from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rowSet = [{} for i in range(9)]
        colSet = [{} for i in range(9)]
        boxSet = [{} for i in range(9)]

        for row in range(9):
            for col in range(9):
                box = (row // 3)*3 -1 + col // 3
                rowSet[row][board[row][col]] = 1
                colSet[col][board[row][col]] = 1
                boxSet[box][board[row][col]] = 1

        basket = [str(i) for i in range(1,10)]
        def dp(i):
            if i == 81:
                return True
            row, col = divmod(i, 9)
            box = (row // 3)*3 -1 + col // 3
            if board[row][col] == '.':
                for num in basket:
                    if num not in rowSet[row] and num not in colSet[col] and num not in boxSet[box]:
                        board[row][col] = num
                        rowSet[row][num] = 1
                        colSet[col][num] = 1
                        boxSet[box][num] = 1
                        if dp(i + 1):
                            return True
                        else:
                            board[row][col] = '.'
                            del rowSet[row][num]
                            del colSet[col][num]
                            del boxSet[box][num]
                return False
            else:
                if dp(i + 1):
                    return True
                else:
                    return False

        dp(0)
        return board


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

x = Solution()
result = x.solveSudoku(board)
print(result)







