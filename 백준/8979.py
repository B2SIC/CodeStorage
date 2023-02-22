import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
data = []
for _ in range(n):
    idx, gold, silver, bronze = map(int, input().split())
    data.append((gold, silver, bronze))

    if idx == k:
        k = (gold, silver, bronze)
data.sort(reverse=True)
for i in range(n):
    if data[i] == k:
        print(i + 1)
        break
