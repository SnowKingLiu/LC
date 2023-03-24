# by:Snowkingliu
# 2023/3/23 09:55


def is_all_empty(n, arr, x, y, queue):
    if arr[x][y] != 1:
        return False
    if queue in arr[x]:
        return False
    if queue in [arr[i][y] for i in range(n)]:
        return False
    _x = x - 1
    _y = y - 1
    while _x >= 0 and _y >= 0:
        if arr[_x][_y] == queue:
            return False
        _x -= 1
        _y -= 1

    _x = x + 1
    _y = y + 1
    while _x < n and _y < n:
        if arr[_x][_y] == queue:
            return False
        _x += 1
        _y += 1

    _x = x - 1
    _y = y + 1
    while _x >= 0 and _y < n:
        if arr[_x][_y] == queue:
            return False
        _x -= 1
        _y += 1

    _x = x + 1
    _y = y - 1
    while _x < n and _y >= 0:
        if arr[_x][_y] == queue:
            return False
        _x += 1
        _y -= 1

    return True


def insert_queen(n, x, queen, arr, maps):
    for y in range(n):
        if is_all_empty(n, arr, x, y, queen):
            arr[x][y] = queen
            if x >= n - 1:
                if queen == 2:
                    insert_queen(n, 0, 3, arr, maps)
                else:
                    maps.append(1)
            else:
                insert_queen(n, x + 1, queen, arr, maps)
            arr[x][y] = 1


def two_n_queen():
    n = int(input())
    arr = []
    maps = []
    for line in range(n):
        arr.append([int(x) for x in input().split(" ") if x != ""])

    insert_queen(n, 0, 2, arr, maps)
    print(len(maps))


if __name__ == "__main__":
    two_n_queen()
