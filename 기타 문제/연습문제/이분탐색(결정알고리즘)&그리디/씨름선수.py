n = int(input())

specs = []
for _ in range(n):
    specs.append(list(map(int, input().split())))

specs.sort(reverse=True)

ans = 0
cur_max = 0
for i in range(n):
    if specs[i][1] > cur_max:
        ans += 1
        cur_max = specs[i][1]
print(ans)