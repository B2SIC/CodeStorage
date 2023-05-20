T = int(input())

for i in range(1, T + 1):
    n = int(input())
    ans = 0

    for k in range(-n, n + 1):
        for j in range(-n, n + 1):
            if (k ** 2) + (j ** 2) <= (n ** 2):
                ans += 1
    print(f"#{i} {ans}")
