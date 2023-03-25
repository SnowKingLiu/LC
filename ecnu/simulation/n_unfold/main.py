from decimal import Decimal


def cache(func):
    cache_dict = {}

    def wrap(a):
        if a in cache_dict:
            return cache_dict[a]
        else:
            res = func(a)
            cache_dict[a] = res
            return res

    return wrap


@cache
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def main():
    x = float(input())
    s = '1'
    e = 1
    i = 1
    while e >= 0.00001:
        e = pow(x, i) / fact(i)
        i += 1
        s = Decimal(s) + Decimal(e)
    print(round(s, 4))


if __name__ == '__main__':
    main()
