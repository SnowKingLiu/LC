# by:Snowkingliu
# 2023/3/1 18:23


def main():
    n, _ = input().split(" ")
    score = 0
    for _ in range(int(n)):
        score += max([int(mm) for mm in input().split(" ")])
    print(score)


if __name__ == "__main__":
    main()
