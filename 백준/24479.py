import sys

sys.setrecursionlimit(10 ** 6)  # 최대 깊이 확장
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = list()
ans = [0 for _ in range(n + 1)]
count = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())

    graph[u].append(v)
    graph[v].append(u)

for gr in graph:
    gr.sort()


def dfs(graph, visited, v):
    visited[v] = True
    result.append(v)

    for x in graph[v]:
        if visited[x] is False:
            dfs(graph, visited, x)


dfs(graph, visited, r)

# 정점 i의 방문 순서 표기
for rs in result:
    ans[rs] = count
    count += 1

# 출력
for an in ans[1:]:
    print(an)
