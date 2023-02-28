# by:Snowkingliu
# 2023/2/28 17:48


def step(state, n, x):
    if state > n or state in x:
        return 0
    if state == n:
        return 1
    return step(state + 1, n, x) + step(state + 2, n, x) + step(state + 3, n, x)


def get_step_num(n, x):
    return step(1, n, x) + step(2, n, x) + step(3, n, x)


def main():
    n, k = [int(i) for i in input().split(" ")]
    x = [int(i) for i in k and input().split(" ") or []]

    print(get_step_num(n, x))


if __name__ == "__main__":
    main()
