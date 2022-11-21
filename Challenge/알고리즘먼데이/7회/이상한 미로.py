# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Unsolved
import sys
import heapq

INF = int(1e18)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
an_list = list(map(int, input().rstrip().split()))

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
print(distance)
