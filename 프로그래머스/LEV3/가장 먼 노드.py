import heapq

INF = int(1e18)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for st, ed in edge:
        graph[st].append((1, ed))
        graph[ed].append((1, st))

    distance = [INF] * (n + 1)

    def dijkstra(v):
        queue = []
        distance[v] = 0
        heapq.heappush(queue, (0, v))

        while queue:
            dist, now = heapq.heappop(queue)

            if distance[now] < dist:
                continue

            for k in graph[now]:  # k[0] = 비용, k[1] = 다음 연결 노드
                cost = dist + k[0]

                if cost < distance[k[1]]:
                    distance[k[1]] = cost
                    heapq.heappush(queue, (cost, k[1]))

        return distance

    dijkstra(1)
    max_dis = 0
    for dis in distance:
        if dis < INF and dis > max_dis:
            max_dis = dis
    return distance.count(max_dis)
