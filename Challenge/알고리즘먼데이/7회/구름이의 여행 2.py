# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
'''
Test Case (Unsolved)
8 11 4
4 2
1 2
1 4
4 5
5 3
3 1
4 6
6 7
7 4
2 8
8 1
'''
import sys

sys.setrecursionlimit(10 ** 6)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
sequence = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(start, v):
    if visited[v]:
        if v == start:
            return True
        return False

    visited[v] = True
    seq.append(v)

    for k in graph[v]:
        if dfs(start, k):
            return True
    return False


ans = int(1e9)
for i in graph[start]:
    visited = [False] * (n + 1)
    visited[start] = True
    seq = [start]
    res = dfs(start, i)
    print(res, seq)

    if res:
        if len(seq) < ans:
            ans = len(seq)

if ans == int(1e9):
    print(-1)
else:
    print(ans)