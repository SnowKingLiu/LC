def main():
    n = int(input())
    s = input()

    output = []
    for ss in s:
        ascii_code = ord(ss)
        ascii_code = (ascii_code - ord('a') + n) % 26 + ord('a')
        output.append(chr(ascii_code))
    print("".join(output))


if __name__ == '__main__':
    main()
