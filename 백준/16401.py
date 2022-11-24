# PyPy3

def is_possible(snack_list, length, m):
    ct = 0

    for snack in snack_list[::-1]:
        if snack >= length:
            ct += (snack // length)

        if ct >= m:
            return True
    return False


m, n = map(int, input().split())
snack_list = list(map(int, input().split()))
snack_list.sort()

st = 1
en = snack_list[-1]

max_mid = 0
while st <= en:
    mid = (st + en) // 2

    if is_possible(snack_list, mid, m):
        if mid > max_mid:
            max_mid = mid
        st = mid + 1
    else:
        en = mid - 1

print(max_mid)