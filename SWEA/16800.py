from math import sqrt

T = int(input())

def getFootStep(x, y):
    return (x - 1) + (y - 1)

for k in range(1, T + 1):
    n = int(input())
    res = n

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            res = min(res, getFootStep(i, n // i))

    print(f"#{k} {res}")
