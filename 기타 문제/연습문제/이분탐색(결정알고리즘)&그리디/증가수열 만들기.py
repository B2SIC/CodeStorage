# deque를 사용하면 조금 더 빠르게 처리가 가능하다.
n = int(input())
n_list = list(map(int, input().split()))

res = 0  # 길이
res_list = []  # 왼쪽, 오른쪽 표시
last_num = -1
while n_list:
    if max(last_num, n_list[0], n_list[-1]) == last_num:
        break

    if len(n_list) == 1:
        res_list.append('L')
        last_num = n_list.pop(0)
    else:
        if n_list[0] < n_list[-1]:
            if last_num < n_list[0]:
                res_list.append('L')
                last_num = n_list.pop(0)
            else:
                res_list.append('R')
                last_num = n_list.pop()
        else:
            if last_num < n_list[-1]:
                res_list.append('R')
                last_num = n_list.pop()
            else:
                res_list.append('L')
                last_num = n_list.pop(0)

    res += 1

print(res)
print("".join(res_list))
