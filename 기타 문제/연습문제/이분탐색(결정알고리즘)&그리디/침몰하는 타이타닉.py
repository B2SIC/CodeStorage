n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

i, j = 0, n - 1
res = 0
while i <= j:
    if n_list[i] + n_list[j] > m:
        res += 1
        j -= 1
    else:
        res += 1
        i += 1
        j -= 1
print(res)
