n, m = map(int, input().split())

s = []
i = 1
while len(s) < max(n, m):
    for j in range(i):
        s.append(i)
    i += 1

sum = 0
for k in range(n, m + 1):
    sum += s[k - 1]

print(sum)
