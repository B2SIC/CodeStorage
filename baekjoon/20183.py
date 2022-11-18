import heapq
import sys

input = sys.stdin.readline
INF = int(1e18)

n, m, a, b, money = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
costs = set()

for _ in range(m):
    u, v, c = map(int, input().rstrip().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
    costs.add(c)


def dijkstra(limit):
    distance = [INF] * (n + 1)
    distance[a] = 0

    queue = []
    heapq.heappush(queue, (0, a))
    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                if i[1] <= limit:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))

    if distance[b] > money:
        return INF
    else:
        return distance[b]


costs = list(costs)
costs.sort()
l = 0
r = len(costs) - 1
min_cost = INF

while l <= r:
    m = (l + r) // 2

    get_min_cost = dijkstra(costs[m])

    if get_min_cost == INF:
        l = m + 1
    else:
        r = m - 1
        min_cost = min(min_cost, costs[m])

if min_cost == INF:
    print(-1)
else:
    print(min_cost)
