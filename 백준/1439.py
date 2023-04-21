s = list(map(int, input()))
r = []

before = -1
for i in range(len(s)):
    if s[i] != before:
        r.append(s[i])
    before = s[i]

ct_0 = 0
ct_1 = 0
for elem in r:
    if elem == 1:
        ct_1 += 1
    else:
        ct_0 += 1

res = min(ct_0, ct_1)
print(res)
