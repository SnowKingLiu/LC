# by:Snowkingliu
# 2023/2/24 17:39


def get_array_num(x):
    return int((x ** 0.5) % 1 == 0)


def get_one_set():
    return {i**2 for i in range(1, int(1e9**0.5))}


def main():
    times = int(input())
    # one_set = get_one_set()
    arr = []
    for idx in range(times):
        arr.append(int(input()))

    for idx in arr:
        x = 8 * idx - 7
        # print(1 if x in one_set else 0)
        print(get_array_num(x))


if __name__ == "__main__":
    main()
