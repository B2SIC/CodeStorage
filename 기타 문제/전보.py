import heapq


INF = int(1e18)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, v = map(int, input().split())
    graph[x].append((y, v))  # 단방향

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for k in graph[now]:  # k[0]: 목적지, k[1]: 비용
            cost = dist + k[1]

            if cost < distance[k[0]]:
                distance[k[0]] = cost
                heapq.heappush(q, (cost, k[0]))

dijkstra(c)
count = 0
max_distance = 0

for dis in distance:
    if dis != INF:
        count += 1
        max_distance = max(max_distance, dis)
print(distance)
print(count - 1, max_distance)
