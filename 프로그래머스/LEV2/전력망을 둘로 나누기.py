from collections import deque


def solution(n, wires):
    answer = int(1e9)
    graph = [set() for _ in range(n + 1)]

    for wire in wires:
        x, y = wire
        graph[x].add(y)
        graph[y].add(x)

    for wire in wires:
        cut_x, cut_y = wire
        graph[cut_x].discard(cut_y)
        graph[cut_y].discard(cut_x)

        # 송전탑 계산
        sum_of_tree = 0
        visited = [0] * (n + 1)
        for i in range(1, n + 1):
            if visited[i] == 0:
                queue = deque([i])
                visited[i] = 1

                while queue:
                    x = queue.popleft()

                    for k in graph[x]:
                        if not visited[k]:
                            queue.append(k)
                            visited[k] = 1
                sum_of_tree = sum(visited)
                break

        # 송전탑 개수 차이가 최소가 되도록 (최대한 비슷하게 맞추기)
        diff = abs(sum_of_tree - (n - sum_of_tree))
        if diff < answer:
            answer = diff

        # 절단 원상 복구
        graph[cut_x].add(cut_y)
        graph[cut_y].add(cut_x)

    return answer
