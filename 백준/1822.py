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

nA, nB = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
A_list.sort()
B_list.sort()

count = 0
ans = []
for num in A_list:
    if not binary_search(B_list, num):
        count += 1
        ans.append(num)

print(count)
print(*ans)
