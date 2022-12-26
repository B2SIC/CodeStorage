from collections import deque


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j and computers[i][j]:
                graph[i].append(j)

    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            queue = deque()
            queue.append(i)
            visited[i] = 1
            while queue:
                x = queue.popleft()

                for k in graph[x]:
                    if not visited[k]:
                        visited[k] = 1
                        queue.append(k)

            answer += 1
    return answer
