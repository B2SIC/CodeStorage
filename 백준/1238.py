import sys
import heapq

input = sys.stdin.readline
n, m, x = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    distance = [INF] * (n + 1)
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

    return distance


n_costs = [0] * (n + 1)
x_go_back_costs = dijkstra(x)

for i in range(1, n + 1):
    n_costs[i] = dijkstra(i)[x]
    n_costs[i] += x_go_back_costs[i]

print(max(n_costs))
