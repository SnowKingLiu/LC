# by:Snowkingliu
# 2023/3/23 11:23


def cache(func):
    cache_dict = {}

    def wrap(n):
        if n in cache_dict:
            return cache_dict[n]
        else:
            res = func(n)
            cache_dict[n] = res
        return res

    return wrap


@cache
def get_fj_str(n):
    base_str = chr(64 + n)
    if n == 1:
        return base_str
    else:
        _fj = get_fj_str(n - 1)
        return "{}{}{}".format(_fj, base_str, _fj)


def main():
    n = int(input())
    s = get_fj_str(n)
    print(s)


if __name__ == "__main__":
    main()
