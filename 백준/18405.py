from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

# s초 후 x, y 위치의 바이러스 종류 출력
s, x, y = map(int, input().rstrip().split())

virus_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] >= 1 and graph[i][j] <= k:
            virus_list.append((graph[i][j], i, j))
virus_list.sort()

queue = deque()
for virus in virus_list:
    num, i, j = virus
    queue.append((i, j))

time = 0
time_size = len(queue)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    if time == s:
        break

    time += 1
    iter_size = 0
    for _ in range(time_size):
        i, j = queue.popleft()

        for r in range(4):
            ni = i + dx[r]
            nj = j + dy[r]

            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue

            if graph[ni][nj] < 1 or graph[ni][nj] > k:
                graph[ni][nj] = graph[i][j]
                queue.append((ni, nj))
                iter_size += 1

    time_size = iter_size

if graph[x - 1][y - 1] >= 1 and graph[x - 1][y - 1] <= k:
    print(graph[x - 1][y - 1])
else:
    print(0)
