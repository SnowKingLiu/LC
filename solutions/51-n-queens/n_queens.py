# by:Snowkingliu
# 2023/2/1 14:25
import numpy as np


class Solution:
    def __init__(self):
        self.n = 0
        self.chessboard = None
        self.chessboards = []

    def solveNQueens(self, n: int):
        self.n = n
        self.chessboard = np.zeros([n, n], dtype=int)
        self.insert_queen(0)
        return self.chessboards

    def replace_list(self):
        output = []
        for line in self.chessboard:
            output.append("".join(["Q" if x else "." for x in line]))
        return output

    def is_all_empty(self, x, y):
        sum_line = self.chessboard[x].sum()
        sum_row = self.chessboard[:, y].sum()
        diagonal = self.chessboard.diagonal(offset=y - x).sum()
        counter_diagonal = (
            np.fliplr(self.chessboard).diagonal(offset=(self.n - 1 - y) - x).sum()
        )
        return sum_line + sum_row + diagonal + counter_diagonal == 0

    def insert_queen(self, y):
        row = self.chessboard[y]
        for x in range(row.size):
            if self.is_all_empty(x, y):
                self.chessboard[x, y] = 1
                if y >= self.n - 1:
                    self.chessboards.append(self.replace_list())
                else:
                    if self.insert_queen(y + 1):
                        return True
                self.chessboard[x, y] = 0
        return False


if __name__ == "__main__":
    for i in range(4, 10):
        s = Solution()
        arr = s.solveNQueens(i)
        print(f"\n{i}\n{arr}")
