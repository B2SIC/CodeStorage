n, m = map(int, input().split())
num_list = list(map(int, input().split()))

lt = 1
rt = sum(num_list)
max_num = max(num_list)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2

    cnt = 1
    partial_sum = 0
    for num in num_list:
        if partial_sum + num <= mid:
            partial_sum += num
        else:
            cnt += 1
            partial_sum = num

    if mid >= max_num and cnt <= m:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)
