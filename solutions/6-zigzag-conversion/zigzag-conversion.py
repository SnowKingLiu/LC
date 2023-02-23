# by:Snowkingliu
# 2023/2/23 11:08


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        line_array = [[] for _ in range(numRows)]

        i = 0
        while i < len(s):
            line_idx = i % (2 * numRows - 2 if numRows > 1 else 1)
            line_idx = line_idx if line_idx < numRows else numRows - (line_idx - numRows) - 2
            line_array[line_idx].append(s[i])
            i += 1
        return "".join(["".join(line_array[i]) for i in range(numRows)])


if __name__ == "__main__":
    solution = Solution()
    print("")
    print(solution.convert("01234567", 1))
    print(solution.convert("01234567", 2))
    print(solution.convert("01234567", 3))
