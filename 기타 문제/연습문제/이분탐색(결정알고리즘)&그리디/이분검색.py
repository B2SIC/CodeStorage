n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

l = 0
r = n - 1

while l <= r:
    mid = (l + r) // 2

    if n_list[mid] == m:
        print(mid + 1)
        break
    elif n_list[mid] < m:
        l = mid + 1
    elif n_list[mid] > m:
        r = mid - 1
