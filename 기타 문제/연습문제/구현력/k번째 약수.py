import sys


# sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())

result = []
for i in range(1, n + 1):
    if n % i == 0:
        result.append(i)

if len(result) < k:
    print(-1)
else:
    print(result[k - 1])
