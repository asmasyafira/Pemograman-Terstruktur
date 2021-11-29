import random


def shuffleString(x, n):
    listResult = []
    for i in range(n):
        randomString = ''.join(random.sample(x, len(x)))
        if randomString not in listResult:
            listResult += [randomString]
    print(listResult)


shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
