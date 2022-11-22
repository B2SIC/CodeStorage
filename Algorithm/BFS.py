from collections import deque


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if visited[i]: continue
            visited[i] = True
            queue.append(i)


# Node: 1 ~ 8
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

bfs(graph, 1, visited)
