import sys

n = int(input())
graph = list()

count = 0
count_list = list()

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) is True:
            result += 1
            count_list.append(count)
            count = 0

print(result)
count_list.sort()
for ct in count_list:
    print(ct)
