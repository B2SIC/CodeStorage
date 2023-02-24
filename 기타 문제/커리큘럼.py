'''
# 1
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
from collections import deque


n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
cost = [0] * (n + 1)

for i in range(1, n + 1):
    stream = list(map(int, input().split()))
    cost[i] = stream[0]
    for k in stream[1:-1]:
        graph[k].append(i)
        indegree[i] += 1

queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

result = cost[:]
while queue:
    x = queue.popleft()

    for k in graph[x]:
        indegree[k] -= 1

        if indegree[k] == 0:
            queue.append(k)
            result[k] = max(result[k], result[x] + cost[k])

for elem in result[1:]:
    print(elem)
