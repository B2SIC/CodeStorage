def dfs(start, weight, t_sum):  # t_sum: 판단을 한 구간의 합
    global res
    # 아직 판단을 안한 구간의 합: (total - t_sum)
    # 현재까지의 무게 합(weight)
    # 이 둘을 더해도 res 보다 작다면 내려가서 가지를 칠 필요가 없다. (어차피 작으니까)
    if (total - t_sum) + weight < res:
        return
    if weight > c:
        return
    if start == n:
        if weight > res:
            res = weight
        return

    dfs(start + 1, weight + badooks[start], t_sum + badooks[start])
    dfs(start + 1, weight, t_sum + badooks[start])

c, n = map(int, input().split())
res = 0
badooks = []  # 바둑이들의 무게 목록
for _ in range(n):
    badooks.append(int(input()))
total = sum(badooks)
dfs(0, 0, 0)
print(res)
