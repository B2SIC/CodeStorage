k, n = map(int, input().split())
num_list = []

lt = 1
rt = 0
for _ in range(k):
    get_num = int(input())
    num_list.append(get_num)
    rt = max(rt, get_num)

ans = 0
while lt <= rt:
    mid = (lt + rt) // 2

    cnt = 0
    for num in num_list:
        cnt += num // mid

    if cnt >= n:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)
