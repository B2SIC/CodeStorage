from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
queue = deque()
ans = 0

start = 1
visited[start] = True

for i in graph[start]:
    queue.append(i)
    visited[i] = True
    ans += 1

while queue:
    x = queue.popleft()

    for i in graph[x]:
        if not visited[i]:
            ans += 1
            visited[i] = True

print(ans)
