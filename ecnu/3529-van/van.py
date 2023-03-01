# by:Snowkingliu
# 2023/3/1 10:37


def main():
    n = int(input())
    arr_list = []
    for nn in range(n):
        if nn == 0:
            arr_list.append([1])
            print(1)
            continue

        arr_line = []
        for m in range(nn + 1):
            arr_line.append(sum(arr_list[nn - 1][m - 1 if m - 1 >= 0 else 0: m + 1]))
        arr_list.append(arr_line)
        print(" ".join([str(a) for a in arr_line]))


if __name__ == "__main__":
    main()
