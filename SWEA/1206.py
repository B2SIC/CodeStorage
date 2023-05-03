for k in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    res = 0
    for i in range(2, n - 2):
        left = max(building[i - 1], building[i - 2])
        right = max(building[i + 1], building[i + 2])

        if building[i] > left and building[i] > right:
            res += min(building[i] - left, building[i] - right)

    print(f"#{k} {res}")
