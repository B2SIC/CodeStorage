s = list(map(int, input()))
res = s[0]

for i in range(1, len(s)):
    if res >= 2 and s[i] >= 2:
        res *= s[i]
    else:
        res += s[i]

print(res)
