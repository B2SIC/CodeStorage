import sys

input = sys.stdin.readline

def binary_search(k):
    s, e = 0, len(mark) - 1
    res = 0
    while s <= e:
        mid = (s + e) // 2

        if k <= int(mark[mid][1]):
            res = mark[mid][0]
            e = mid - 1
        elif k > int(mark[mid][1]):
            s = mid + 1
    return res

n, m = map(int, input().rstrip().split())
mark = [input().rstrip().split() for _ in range(n)]

for _ in range(m):
    force = int(input())
    print(binary_search(force))
