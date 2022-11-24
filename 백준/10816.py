n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def lower_idx(num_list, num):
    l = 0
    r = len(num_list)

    while l < r:
        m = (l + r) // 2

        if num_list[m] >= num:
            r = m
        else:
            l = m + 1

    return l

def upper_idx(num_list, num):
    l = 0
    r = len(num_list)

    while l < r:
        m = (l + r) // 2

        if num_list[m] > num:
            r = m
        else:
            l = m + 1
    return l

for num in m_list:
    print(upper_idx(n_list, num) - lower_idx(n_list, num), end=' ')
