def palindrome_counter(l: list):
    cnt = 0
    for i in range(3):
        if l[i] == l[i + 4] and l[i + 1] == l[i + 4 - 1]:
            cnt += 1
    return cnt

ans = 0
graph = []
for _ in range(7):
    graph.append(list(map(int, input().split())))

# 행 기반
for line in graph:
    ans += palindrome_counter(line)

# 열 기반
for i in range(7):
    num_list = []
    for j in range(7):
        num_list.append(graph[j][i])
    ans += palindrome_counter(num_list)

print(ans)
