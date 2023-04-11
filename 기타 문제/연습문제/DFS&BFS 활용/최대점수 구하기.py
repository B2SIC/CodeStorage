def dfs(v, score, time):
    global res
    if time > m:
        return
    if v == n:
        if score > res:
            res = score
        return

    dfs(v + 1, score + scores[v], time + times[v])
    dfs(v + 1, score, time)

n, m = map(int, input().split())
scores, times = [], []
res = 0
for _ in range(n):
    x, y = map(int, input().split())  # 문제 점수, 걸리는 시간
    scores.append(x)
    times.append(y)

dfs(0, 0, 0)
print(res)
