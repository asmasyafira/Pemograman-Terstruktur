def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial (n - 1)

def C(x, y):
    result = faktorial(x)//(faktorial(y)*faktorial(x-y))
    print ("C(5,3) =", result)

def P(x, y):
    result = faktorial(x)//faktorial(x-y)
    print ("P(10, 7) =", result)

C(5, 3)
P(10, 7)
