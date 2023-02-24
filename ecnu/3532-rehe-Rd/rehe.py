# by:Snowkingliu
# 2023/2/24 17:39

def main():
    print("\nPlease input request time.")
    times = input()
    arr = []
    if not times.isalnum() or not (1 < int(times) < 1500000):
        print(f"Invalid input")
        return
    for idx in range(int(times)):
        a_idx = input()
        if not times.isalnum() or not (1 <= int(a_idx) <= int(10**9)):
            print(f"Invalid input")
            return
        arr.append(int(a_idx))

    res = [str(get_array_num(a_idx)) for a_idx in arr]
    for r in res:
        print(r)
    # return '\n'.join(res)


def get_array_num(a_idx):
    return int((-1 + (1 + 8 * (a_idx - 1))**0.5) % 1 == 0)


if __name__ == '__main__':
    main()
