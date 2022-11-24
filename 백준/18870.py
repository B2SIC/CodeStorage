n = int(input())

n_list = list(map(int, input().split()))
b_n_list = list(set(n_list))
b_n_list.sort()

def binary_search(num_list, target):
    st = 0
    en = len(num_list) - 1

    while st <= en:
        m = (st + en) // 2

        if num_list[m] > target:
            en = m - 1
        elif num_list[m] < target:
            st = m + 1
        else:
            return m
    return 0

for num in n_list:
    print(binary_search(b_n_list, num), end=' ')
