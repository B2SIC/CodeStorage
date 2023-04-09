def dfs(depth):
    if depth == m:
        print(*p)
        return

    before = -1
    for i in range(len(arr)):
        if not visited[i] and arr[i] != before:
            visited[i] = 1
            p[depth] = arr[i]
            before = arr[i]
            dfs(depth + 1)
            visited[i] = 0


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * len(arr)
p = [0] * m
dfs(0)
