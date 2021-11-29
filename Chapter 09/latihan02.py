def bintang(n):
    for i in range(n):
        print(("*" * (1 + 2 * i)).center(2 * n - 1))


bintang(4)
