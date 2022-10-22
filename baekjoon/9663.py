n = int(input())

is_used1 = [0] * n
is_used2 = [0] * (2 * n - 1)
is_used3 = [0] * (2 * n - 1)

ans = 0


def func(x):
    global ans
    if x == n:
        ans += 1
        return

    for y in range(n):
        if is_used1[y] == 0 and is_used2[x + y] == 0 and is_used3[x - y + n - 1] == 0:
            is_used1[y] = 1
            is_used2[x + y] = 1
            is_used3[x - y + n - 1] = 1
            func(x + 1)
            is_used1[y] = 0
            is_used2[x + y] = 0
            is_used3[x - y + n - 1] = 0


func(0)
print(ans)
