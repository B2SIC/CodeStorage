import sys

n = int(input()) # Computer 수
m = int(input()) # 연결 쌍의 수

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(graph, v):
  visited[v] = 1

  for i in graph[v]:
    if visited[i] == 0:
      dfs(graph, i)

dfs(graph, 1)

print(sum(visited) - 1)
