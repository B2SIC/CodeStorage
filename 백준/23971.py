h, w, n, m = map(int, input().split())
x, y = 0, 0
for _ in range(0, h, n + 1):
    x += 1
for j in range(0, w, m + 1):
    y += 1
print(x * y)
