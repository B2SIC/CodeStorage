# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import heapq

INF = int(1e18)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
an_list = [0] + list(map(int, input().rstrip().split()))

graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
distance = [[INF for _ in range(10)] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start = 1
ans = -1
q = []
distance[start][0] = 0
heapq.heappush(q, (distance[start][0], start, 0))

while q:
    dist, now, prev = heapq.heappop(q)
    print(dist, now, prev)
    print(distance[now][prev])

    if distance[now][prev] < dist:
        continue

    if now == n:
        ans = dist
        break

    for i in graph[now]:
        if now == 1 or prev % an_list[now] == i[0] % an_list[now]:
            # print(prev, '->', now, '->', i[0])
            cost = dist + i[1]

            if cost < distance[i[0]][now % an_list[i[0]]]:
                distance[i[0]][now % an_list[i[0]]] = cost
                heapq.heappush(q, (cost, i[0], now % an_list[i[0]]))

print(ans)
