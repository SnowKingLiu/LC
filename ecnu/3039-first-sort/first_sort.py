# by:Snowkingliu
# 2023/3/6 15:56


def main():
    t = int(input())
    res = []
    for tt in range(t):
        input()
        nums = input().split(" ")
        result = {i: [] for i in range(10)}
        for num in nums:
            if num[0] == "-":
                result[int(num[1])].append(int(num))
            else:
                result[int(num[0])].append(int(num))
        r = []
        for i in range(9, -1, -1):
            r.extend(sorted(result[i]))
        if r:
            res.append(r)

    for idx, r in enumerate(res):
        print(f"case #{idx}:")
        print(" ".join([str(rr) for rr in r]))


if __name__ == "__main__":
    main()
