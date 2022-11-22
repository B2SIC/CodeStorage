import heapq
import sys

input = sys.stdin.readline
INF = int(1e18)

n, m, k = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, c = map(int, input().rstrip().split())
    graph[v].append((u, c))

interview_place = list(map(int, input().rstrip().split()))

queue = []

for point in interview_place:
    distance[point] = 0
    heapq.heappush(queue, (0, point))

while queue:
    dist, now = heapq.heappop(queue)

    if distance[now] < dist:
        continue

    for v, c in graph[now]:
        cost = dist + c

        if cost < distance[v]:
            distance[v] = cost
            heapq.heappush(queue, (cost, v))

max_city_num = 0
max_dist = 0

for i in range(1, n + 1):
    if distance[i] != INF and distance[i] > 0:
        if distance[i] > max_dist:
            max_dist = distance[i]
            max_city_num = i

print(max_city_num)
print(max_dist)
