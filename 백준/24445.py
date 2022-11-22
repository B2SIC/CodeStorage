from collections import deque
import sys

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = list()
answer = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for gr in graph:
    gr.sort(reverse=True)  # 내림차순

queue = deque()
queue.append(r)
visited[r] = True

while queue:
    val = queue.popleft()
    result.append(val)

    for x in graph[val]:
        if visited[x] is False:
            visited[x] = True
            queue.append(x)

count = 1
for rs in result:
    answer[rs] = count
    count += 1

for ans in answer[1:]:
    print(ans)
