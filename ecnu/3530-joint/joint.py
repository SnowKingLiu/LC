# by:Snowkingliu
# 2023/3/1 10:08


def main():
    input()
    arr = [x for x in input().split(" ")]
    arr.sort(reverse=True)
    print("".join(arr))


if __name__ == "__main__":
    main()
