# by:Snowkingliu
# 2023/3/6 18:01

def main2():
    sort_type = input()
    flag = [0] * 1001
    numbers = []
    for num in input().split(" "):
        num = int(num)
        if flag[num]:
            continue
        flag[num] = 1
        numbers.append(num)
    numbers.sort()
    if sort_type == "D":
        numbers = numbers[::-1]
    print(" ".join([str(n) for n in numbers]))


def main():
    sort_type = input()
    num_set = set()
    for num in input().split(" "):
        num_set.add(int(num))

    numbers = sorted(list(num_set))
    if sort_type == "D":
        numbers = numbers[::-1]
    print(" ".join([str(n) for n in numbers]))


if __name__ == '__main__':
    main()
