'''
1697번 숨바꼭질

1차원 BFS 적용하기
'''

from collections import deque
import sys


input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().rstrip().split())

dist = [-1] * (100000 + 1)

queue = deque()
queue.append(n)
dist[n] = 0

while queue:
    x = queue.popleft()

    for i in [x - 1, x + 1, x * 2]:
        if i < 0 or i > 100000 or dist[i] != -1:
            continue
        dist[i] = dist[x] + 1
        queue.append(i)

print(dist[k])
