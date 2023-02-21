from collections import deque


def solution(n, computers):
    answer = 0

    computers = [0] + computers
    visited = [0] * (n + 1)  # 방문 여부 표시

    for i in range(1, n + 1):
        if not visited[i]:
            queue = deque([i])
            visited[i] = 1
            answer += 1

            while queue:
                v = queue.popleft()

                for k in range(len(computers[v])):
                    if k + 1 == v:
                        continue

                    if computers[v][k] and not visited[k + 1]:
                        queue.append(k + 1)
                        visited[k + 1] = 1

    return answer
