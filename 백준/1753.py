import sys
import heapq

input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())

INF = int(1e9)
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# dijkstra
queue = []
heapq.heappush(queue, (0, start))
distance[start] = 0

while queue:
    dist, now = heapq.heappop(queue)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
