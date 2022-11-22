from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

input_list = list(map(int, input().split()))

graph = [[] for _ in range(input_list[0] + 1)]

for i in range(input_list[1]):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[start].sort()
    graph[end].append(start)
    graph[end].sort()

visited = [False] * (input_list[0] + 1)
dfs(graph, input_list[2], visited)

print()
visited = [False] * (input_list[0] + 1)
bfs(graph, input_list[2], visited)