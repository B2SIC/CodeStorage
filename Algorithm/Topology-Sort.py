# 위상정렬 시간복잡도: O(V + E)
from collections import deque


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, v + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    v = queue.popleft()
    result.append(v)

    for k in graph[v]:
        indegree[k] -= 1

        if indegree[k] == 0:
            queue.append(k)

print(*result)




