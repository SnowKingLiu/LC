# by:Snowkingliu
# 2023/2/28 16:24


def main():
    m, n, k = [int(v) for v in input().split(" ")]

    m_idx = 0
    n_idx = 0
    for idx in range(k):
        m_idx = m_idx % m + 1
        n_idx = n_idx % n + 1
        print(f"{m_idx} {n_idx}")


if __name__ == "__main__":
    main()
