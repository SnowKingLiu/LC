# by:Snowkingliu
# 2023/2/1 14:42
import numpy as np
import pandas as pd


class Solution:
    def isValidSudokuPd(self, board: list[list[str]]) -> bool:
        df_board = pd.DataFrame(board)
        df_board = df_board.replace(".", np.NaN)
        # Columns
        for col in range(9):
            if df_board[col][df_board[col].notna()].value_counts().max() > 1:
                return False
        # Line
        for line in range(9):
            if df_board.loc[line][df_board.loc[line].notna()].value_counts().max() > 1:
                return False
        # Region
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                df_local = (
                    df_board.loc[x : x + 2][range(y, y + 3)].apply(pd.Series).stack()
                )
                if df_local.value_counts().max() > 1:
                    return False
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Columns
        for col_idx in range(9):
            col = [line[col_idx] for line in board if line[col_idx] != "."]
            if len(col) > len(set(col)):
                return False
        # Line
        for line_idx in range(9):
            line = [item for item in board[line_idx] if item != "."]
            if len(line) > len(set(line)):
                return False
        # Region
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                board_local = board[x : x + 3]
                region = [
                    item
                    for line in board_local
                    for item in line[y : y + 3]
                    if item != "."
                ]
                if len(region) > len(set(region)):
                    return False
        return True


if __name__ == "__main__":
    _board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    # _board = [
    #     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    # ]

    print(Solution().isValidSudoku(_board))
