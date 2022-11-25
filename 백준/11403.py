from collections import deque

n = int(input())

adj_matrix = []
return_matrix = []
for _ in range(n):
    adj_matrix.append(list(map(int, input().split())))

queue = deque()

for i in range(n):
    visited = [0] * n
    queue.append(i)

    while queue:
        x = queue.popleft()

        for k in range(len(adj_matrix[x])):
            if adj_matrix[x][k] == 1 and not visited[k]:
                visited[k] = 1
                queue.append(k)

    return_matrix.append(visited)

for mat in return_matrix:
    print(*mat)
