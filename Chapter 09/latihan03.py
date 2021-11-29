def bintang(n):
    for i in range(n):
        print(("*" * (2 * i + 1)).center(2 * n - 1))

    for i in range(n):
        i = n - i - 1
        print(("*" * (2 * i - 1)).center(2 * n - 1))


def belahKetupat(n):
    a = ((n//2) + 1)
    bintang(a)


belahKetupat(7)
