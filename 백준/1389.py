import sys
from collections import deque


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = sys.maxsize
min_sum = sys.maxsize
for start in range(1, n + 1):
    sum = 0
    for end in range(1, n + 1):
        if start != end:
            queue = deque()
            queue.append(start)

            visited = [False] * (n + 1)
            visited[start] = True
            flag = False

            lev = 0
            while queue:
                for _ in range(len(queue)):
                    x = queue.popleft()

                    for i in graph[x]:
                        if i == end:
                            flag = True
                            break
                        if not visited[i]:
                            queue.append(i)
                            visited[i] = True
                lev += 1

                if flag:
                    break

            sum += lev

    if min_sum > sum:
        min_sum = sum
        ans = start

print(ans)
