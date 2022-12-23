from collections import deque
import sys


input = sys.stdin.readline

n, k, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + m + 1)]
ht = n + 1
for _ in range(m):
    hyper_tubes = list(map(int, input().rstrip().split()))

    for i in hyper_tubes:
        graph[i].append(ht)
        graph[ht].append(i)

    ht += 1

dist = [0] * (n + m + 1)
visited = [0] * (n + m + 1)
queue = deque([1])
visited[1] = 1

while queue:
    x = queue.popleft()

    if x == n:
        break

    for k in graph[x]:
        if not visited[k]:
            visited[k] = 1
            dist[k] = dist[x] + 1
            queue.append(k)

if n != 1 and dist[n] == 0:
    print(-1)
else:
    print(dist[n] // 2 + 1)
