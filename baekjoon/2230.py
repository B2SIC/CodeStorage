import sys

n, m = map(int, input().split())

n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort()

st = 0
en = 0
ans = sys.maxsize

while en < n:
    if st == en:
        en += 1
    else:
        calc = n_list[en] - n_list[st]
        if calc >= m:
            if calc < ans:
                ans = calc
            st += 1
        else:
            en += 1

print(ans)
