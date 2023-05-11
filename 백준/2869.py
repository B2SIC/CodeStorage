from math import ceil

a, b, v = map(int, input().split())

x = ceil((v - a) / (a - b))
print(x + 1)