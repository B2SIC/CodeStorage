n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

max_sum = 0

# 각 행의 합
for line in graph:
    max_sum = max(max_sum, sum(line))

# 각 열의 합
for i in range(n):
    partial_sum = 0
    for j in range(n):
        partial_sum += graph[j][i]
    max_sum = max(max_sum, partial_sum)

# 대각선 합 (좌 -> 우)
partial_sum = 0
for i in range(n):
    partial_sum += graph[i][i]
max_sum = max(max_sum, partial_sum)

# 대각선 합 (우 -> 좌)
partial_sum = 0
for i in range(n):
    partial_sum += graph[i][n - 1 - i]
max_sum = max(max_sum, partial_sum)

print(max_sum)
