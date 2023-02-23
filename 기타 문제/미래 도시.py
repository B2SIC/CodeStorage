import heapq


INF = int(1e18)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())  # 1 -> K -> X

def dijkstra(start, target):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for k in graph[now]:  # k[0]: 연결 노드 번호, k[1]: 거리
            cost = dist + k[1]

            if cost < distance[k[0]]:
                distance[k[0]] = cost
                heapq.heappush(q, (cost, k[0]))
    print(distance)
    return distance[target]


result = dijkstra(1, k) + dijkstra(k, x)
if result >= INF:
    print(-1)
else:
    print(result)
