from collections import defaultdict
import sys


input = sys.stdin.readline
INF = int(1e18)

n, m = map(int, input().rstrip().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, l = map(int, input().rstrip().split())
    graph[a][b] = l

c = int(input())
c_list = list(map(int, input().rstrip().split()))

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_dis = INF
back_and_forth = [0] * (n + 1)
for i in range(1, n + 1):
    for j in c_list:
        back_and_forth[i] = max(back_and_forth[i], graph[i][j] + graph[j][i])

    min_dis = min(min_dis, back_and_forth[i])

for i in range(1, n + 1):
    if min_dis == back_and_forth[i]:
        print(i, end=' ')
