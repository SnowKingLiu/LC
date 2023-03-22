# by:Snowkingliu
# 2023/3/16 16:12
def satisfy(ch):
    bad = "Bad"
    good = "Good"

    left_arc = 0
    plus_count = 0
    ch_list = list(ch)
    last_char = ""
    while ch_list:
        char = ch_list.pop(0)
        if char == "(":
            if last_char not in ["", "+", "("]:
                return bad
            left_arc += 1
            if plus_count:
                plus_count -= 1
        elif char == ")":
            if last_char in ["(", "+"] or left_arc <= 0:
                return bad
            if plus_count:
                plus_count -= 1
            left_arc -= 1
        elif char == "+":
            if left_arc == 0 or last_char in ["+", "("]:
                return bad
            plus_count += 1
        else:
            if last_char not in ["", "(", "+"]:
                return bad
        last_char = char
    return good if left_arc == 0 and last_char not in ["(", "+", ""] else bad


def main():
    n = int(input())
    result = []
    for _ in range(n):
        ch = input()
        res = satisfy(ch)
        result.append(res)

    for res in result:
        print(res)


if __name__ == "__main__":
    main()
