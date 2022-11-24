n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binary_search(num_list, num):
    l = 0
    r = len(num_list) - 1

    while l <= r:
        m = (l + r) // 2

        if num_list[m] == num:
            return 1
        elif num_list[m] > num:
            r = m - 1
        else:
            l = m + 1

    return 0

for num in m_list:
    print(binary_search(n_list, num))
