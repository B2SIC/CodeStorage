'''
6118번 숨바꼭질

BFS를 이용한 그래프 탐색 + 거리 계산
'''

from collections import deque
import sys


input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    ai, bi = map(int, input().rstrip().split())
    graph[ai].append(bi)
    graph[bi].append(ai)

visited = [0] * (n + 1)

queue = deque()
queue.append(1)
visited[1] = 1

while queue:
    x = queue.popleft()

    for i in graph[x]:
        if not visited[i]:
            queue.append(i)
            visited[i] += visited[x] + 1

max_dis = max(visited)

print(visited.index(max_dis), max_dis - 1, visited.count(max_dis))
