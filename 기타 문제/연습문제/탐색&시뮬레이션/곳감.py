from collections import deque


n = int(input())

graph = []
for _ in range(n):
    graph.append(deque(list(map(int, input().split()))))

m = int(input())
for _ in range(m):
    row, direction, count = map(int, input().split())
    row -= 1

    # Deque 활용
    if direction:
        for _ in range(count):
            graph[row].appendleft(graph[row].pop())
    else:
        for _ in range(count):
            graph[row].append(graph[row].popleft())

# 모래시계 영역 계산
ans = 0
s = 0
e = n - 1
for i in range(n):
    for j in range(s, e + 1):
        ans += graph[i][j]

    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(ans)
