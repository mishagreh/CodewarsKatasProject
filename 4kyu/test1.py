def sum(n=100_000_000):
    return (n*(n-1)) // 2


def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s


if __name__ == '__main__':
    print(sum())
    print(while_loop())
