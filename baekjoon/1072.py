x, y = map(int, input().split())

z = (100 * y) // x

if z >= 99:
    print(-1)
else:
    start = 1
    end = x

    result = 0
    while start <= end:
        mid = (start + end) // 2

        new_x = x + mid
        new_y = y + mid
        new_z = int((new_y / new_x) * 100)

        if z < new_z:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)
