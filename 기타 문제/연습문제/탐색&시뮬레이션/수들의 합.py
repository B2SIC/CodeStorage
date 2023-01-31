n, m = map(int, input().split())
n_list = list(map(int, input().split()))

i, j = 0, 0
check_sum = n_list[0]
ans = 0
while i < n or j < n:
    if check_sum >= m:
        if check_sum == m:
            ans += 1
        check_sum -= n_list[i]
        i += 1
    elif check_sum < m:
        j += 1
        if j >= n:
            break
        check_sum += n_list[j]

print(ans)
