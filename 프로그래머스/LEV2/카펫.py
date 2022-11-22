def solution(brown, yellow):
    total_block = brown + yellow

    for x in range(3, total_block + 1):
        if total_block % x == 0:
            y = total_block // x

            if (x - 2) * (y - 2) == yellow:
                if x > y:
                    return [x, y]
                else:
                    return [y, x]
