def binary_search(num_list, target):
    st = 0
    en = len(num_list) - 1

    while st <= en:
        mid = (st + en) // 2

        if num_list[mid] < target:
            st = mid + 1
        elif num_list[mid] > target:
            en = mid - 1
        else:
            return True
    return False

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    if binary_search(n_list, num):
        print(1, end=' ')
    else:
        print(0, end=' ')
