from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
mid_num = (n + 1) // 2

bigger_graph = [[] for _ in range(n + 1)]
smaller_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().rstrip().split())
    bigger_graph[y].append(x)
    smaller_graph[x].append(y)


def bfs(n, mid_num, graph):
    solution = 0
    for i in range(1, n + 1):
        queue = deque([i])
        visited = [0] * (n + 1)
        visited[i] = 1
        cnt = 0

        while queue:
            x = queue.popleft()

            for k in graph[x]:
                if not visited[k]:
                    visited[k] = 1
                    queue.append(k)
                    cnt += 1
        if cnt >= mid_num:
            solution += 1
    return solution


bead = 0
for graph in [bigger_graph, smaller_graph]:
    bead += bfs(n, mid_num, graph)
print(bead)
