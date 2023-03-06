# by:Snowkingliu
# 2023/3/6 16:41


def get_byte_num(num):
    return bin(2**64 + num)[-64:].count("1")


def main():
    t = int(input())
    res = []
    for tt in range(t):
        input()
        nums = input().split(" ")
        result = {}
        for num in nums:
            one_count = get_byte_num(int(num))
            result[one_count] = [int(num), *result.get(one_count, [])]
        r = []
        for i in sorted(result.keys())[::-1]:
            r.extend(sorted(result[i]))
        if r:
            res.append(r)

    for idx, r in enumerate(res):
        print(f"case #{idx}:")
        print(" ".join([str(rr) for rr in r]))


if __name__ == "__main__":
    main()
    # print(get_byte_num(100))
    # print(get_byte_num(15))
