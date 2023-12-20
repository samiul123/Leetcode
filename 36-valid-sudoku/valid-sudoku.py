from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = 9, 9
        for i in range(row):
            row_items = set()
            for j in range(col):
                if board[i][j] != ".":
                    if board[i][j] in row_items:
                        return False
                    row_items.add(board[i][j])

        for j in range(col):
            col_items = set()
            for i in range(row):
                if board[i][j] != ".":
                    if board[i][j] in col_items:
                        return False
                    col_items.add(board[i][j])

        for i in range(0, row, 3):
            for j in range(0, col, 3):
                items = set()
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        if board[m][n] != ".":
                            if board[m][n] in items:
                                return False
                            items.add(board[m][n])

        return True
