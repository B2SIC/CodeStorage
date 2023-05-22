x = int(input())

i, j = 0, 0
start = 1
d = 5
while start + d < x:
    start += d
    d += 4
    j += 2

x = x - start
direction = 0  # 0: down, 1: up
while x > 0:
    if direction:
        i += 1
        x -= 1
        while i != 0 and x > 0:
            i -= 1
            j += 1
            x -= 1
        direction = 0
    else:
        j += 1
        x -= 1
        while j != 0 and x > 0:
            i += 1
            j -= 1
            x -= 1
        direction = 1

print(f"{i + 1}/{j + 1}")
