def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append([int(x) for x in input().split(' ')])

    total = 0
    for i in range(n - 1):
        for j in range(n - 1):
            if i + j == n - 1:
                continue
            total += arr[i][j]
    print(total)


if __name__ == '__main__':
    main()
