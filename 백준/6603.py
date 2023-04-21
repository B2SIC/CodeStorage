def dfs(depth, start):
    if depth == 6:
        print(*p)
        return

    for i in range(start, k):
        p[depth] = nums[i]
        dfs(depth + 1, i + 1)

while True:
    get_line = list(map(int, input().split()))

    k = get_line[0]
    if k == 0:
        break

    nums = get_line[1:]
    p = [0] * 6
    dfs(0, 0)
    print()
