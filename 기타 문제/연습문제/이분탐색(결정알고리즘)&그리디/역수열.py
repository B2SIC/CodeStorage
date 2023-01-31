n = int(input())
n_list = list(map(int, input().split()))

res = [-1] * n

for i in range(1, n + 1):
    cnt = n_list[i - 1]

    j = 0
    while cnt:
        if res[j] == -1:
            cnt -= 1
        j += 1

    for k in range(j, n):
        if res[k] == -1:
            res[k] = i
            break

print(*res)
