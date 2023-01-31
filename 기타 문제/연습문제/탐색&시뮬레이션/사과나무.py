n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = 0
s = e = n // 2
for i in range(n):
    for j in range(s, e + 1):
        ans += graph[i][j]

    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(ans)
