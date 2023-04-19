n = int(input())
line = list(map(int, input().split()))
res = [0] * n

for i in range(n):
    t = line[i] + 1
    find_idx = -1
    while t > 0:
        find_idx += 1
        if res[find_idx] == 0:
            t -= 1
    res[find_idx] = i + 1

print(*res)
