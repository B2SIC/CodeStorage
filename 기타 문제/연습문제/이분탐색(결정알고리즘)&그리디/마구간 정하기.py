n, c = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
num_list.sort()

lt = num_list[0]
rt = num_list[-1] - num_list[0]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2

    # 말 배치
    cnt = 1  # 제일 왼쪽에 말은 고정, 두 말의 거리가 최대가 되도록 하기 위함.
    std = num_list[0]
    for num in num_list[1:]:
        if num - std >= mid:
            std = num
            cnt += 1

    if cnt >= c:
        res = mid
        lt = mid + 1
    elif cnt < c:
        rt = mid - 1

print(res)
