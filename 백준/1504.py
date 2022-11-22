import sys
import heapq

input = sys.stdin.readline
n, e = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n + 1)]
start = 1

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


# dijkstra
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


s_to_v1 = dijkstra(start)[v1]
s_to_v2 = dijkstra(start)[v2]

dijk_v1 = dijkstra(v1)
dijk_v2 = dijkstra(v2)

v1_to_v2 = dijk_v1[v2]
v2_to_v1 = dijk_v2[v1]

v2_to_n_val = dijk_v2[n]
v1_to_n_val = dijk_v1[n]

# 1 -> v1 -> v2 -> n
ans = s_to_v1 + v1_to_v2 + v2_to_n_val
# 1 -> v2 -> v1 -> n
ans = min(ans, s_to_v2 + v2_to_v1 + v1_to_n_val)

if ans >= INF:
    print(-1)
else:
    print(ans)
