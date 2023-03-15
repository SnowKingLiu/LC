# by:Snowkingliu
# 2023/3/15 11:18


def cache(func):
    cache_list = {}

    def wrap(arr, m):
        arg = "".join([str(z) for c in arr for z in c])
        if arg in cache_list:
            return cache_list[arg]
        res = func(arr, m)
        cache_list[arg] = res
        return res

    return wrap


@cache
def get_max_node_num(arr, m):
    if m == 1:
        return 2 if arr[0][0] == "Y" else 0

    max_num = 0
    for i in range(m):
        if max_num >= m - i:
            break
        for j in range(m):
            if arr[i][j] != "Y":
                continue
            new_arr = [
                [arr[x][y] for y in range(m) if y != j and y != i]
                for x in range(m)
                if x != i and x != j
            ]
            if new_arr:
                n = len(new_arr[0])
                num = 2 + get_max_node_num(new_arr, n)
            else:
                num = 2
            max_num = num if num > max_num else max_num
    return max_num


def main():
    n = int(input())
    res = []
    for _ in range(n):
        m = int(input())
        arr = []
        for _ in range(m):
            arr.append(list(input()))

        arr = [["N" if i >= j else arr[i][j] for j in range(m)] for i in range(m)]
        res.append(get_max_node_num(arr, m))

    for r in res:
        print(r)


if __name__ == "__main__":
    main()
