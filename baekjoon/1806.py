import sys

n, s = map(int, input().split())

n_list = list(map(int, input().split()))

en = 0
ans = sys.maxsize
tot = n_list[0]

for st in range(0, n):
    while en < n and tot < s:
        en += 1

        if en != n:
            tot += n_list[en]

    if en == n:
        break

    ans = min(ans, en - st + 1)
    tot -= n_list[st]

if ans == sys.maxsize:
    print(0)
else:
    print(ans)
