# Unsolved

n, m = map(int, input().split())
cctv_map = list()
for _ in range(n):
    cctv_map.append(
        list(map(int, input().split()))
    )

cctv1_x = [0, 0, -1, 1]
cctv1_y = [1, -1, 0, 0]
cctv2 = [0, 1]
cctv3_x = [-1, 1, -1, 1]
cctv3_y = [1, 1, -1, -1]
cctv4 = [1, 0, 3, 2]

ans = 64

def cctv_check(cctv_map, cctv_list):
    global ans
    if len(cctv_list) == 0:
        ans = 1
        return

    x, y, cctv_num = cctv_list.pop(0)

    if cctv_num == 1 or cctv_num == 3:
        if cctv_num == 1:
            nx_cctv_x = cctv1_x
            nx_cctv_y = cctv1_y
        elif cctv_num == 3:
            nx_cctv_x = cctv3_x
            nx_cctv_y = cctv3_y

        for i in range(4):
            cctv_map_tmp = []
            cctv_map_tmp[:] = [item[:] for item in cctv_map]
            nx = x + nx_cctv_x[i]
            ny = y + nx_cctv_y[i]
            while True:
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    break

                if cctv_map[nx][ny] == 6:
                    break

                if cctv_map[nx][ny] == 0:
                    cctv_map[nx][ny] = '#'

                nx = nx + nx_cctv_x[i]
                ny = ny + nx_cctv_y[i]

            if len(cctv_list) != 0:
                cctv_check(cctv_map, cctv_list)
            else:
                count_zero = 0
                for cctv_line in cctv_map:
                    count_zero += cctv_line.count(0)

                if count_zero < ans:
                    ans = count_zero

            cctv_map[:] = cctv_map_tmp

        cctv_list.insert(0, [x, y, cctv_num])

    elif cctv_num == 2:
        for i in range(2):
            cctv_map_tmp = []
            cctv_map_tmp[:] = [item[:] for item in cctv_map]
            if cctv2[i] == 0:
                # 좌우 0
                ny = y + 1
                while True:
                    if ny >= m:
                        break

                    if cctv_map[x][ny] == 6:
                        break

                    if cctv_map[x][ny] == 0:
                        cctv_map[x][ny] = '#'

                    ny += 1

                ny = y - 1
                while True:
                    if ny < 0:
                        break

                    if cctv_map[x][ny] == 6:
                        break

                    if cctv_map[x][ny] == 0:
                        cctv_map[x][ny] = '#'

                    ny -= 1
            else:
                nx = x + 1
                while True:
                    if nx >= n:
                        break

                    if cctv_map[nx][y] == 6:
                        break

                    if cctv_map[nx][y] == 0:
                        cctv_map[nx][y] = '#'

                    nx += 1

                nx = x - 1
                while True:
                    if nx < 0:
                        break

                    if cctv_map[nx][y] == 6:
                        break

                    if cctv_map[nx][y] == 0:
                        cctv_map[nx][y] = '#'

                    nx -= 1

            if len(cctv_list) != 0:
                cctv_check(cctv_map, cctv_list)
            else:
                count_zero = 0
                for cctv_line in cctv_map:
                    count_zero += cctv_line.count(0)

                if count_zero < ans:
                    ans = count_zero

            cctv_map[:] = cctv_map_tmp
        cctv_list.insert(0, [x, y, cctv_num])

    elif cctv_num == 4:
        for i in range(4):
            cctv_map_tmp = []
            cctv_map_tmp[:] = [item[:] for item in cctv_map]

            if cctv4[i] <= 1:
                # 좌우 0
                ny = y + 1
                while True:
                    if ny >= m:
                        break

                    if cctv_map[x][ny] == 6:
                        break

                    if cctv_map[x][ny] == 0:
                        cctv_map[x][ny] = '#'

                    ny += 1

                ny = y - 1
                while True:
                    if ny < 0:
                        break

                    if cctv_map[x][ny] == 6:
                        break

                    if cctv_map[x][ny] == 0:
                        cctv_map[x][ny] = '#'

                    ny -= 1

                if cctv4[i] == 0:
                    nx = x + 1

                    while True:
                        if nx >= n:
                            break

                        if cctv_map[nx][y] == 6:
                            break

                        if cctv_map[nx][y] == 0:
                            cctv_map[nx][y] = '#'

                        nx += 1
                else:
                    nx = x - 1

                    while True:
                        if nx < 0 :
                            break

                        if cctv_map[nx][y] == 6:
                            break

                        if cctv_map[nx][y] == 0:
                            cctv_map[nx][y] = '#'

                        nx -= 1
            elif cctv4[i] >= 2:
                nx = x + 1
                while True:
                    if nx >= n:
                        break

                    if cctv_map[nx][y] == 6:
                        break

                    if cctv_map[nx][y] == 0:
                        cctv_map[nx][y] = '#'

                    nx += 1

                nx = x - 1
                while True:
                    if nx < 0:
                        break

                    if cctv_map[nx][y] == 6:
                        break

                    if cctv_map[nx][y] == 0:
                        cctv_map[nx][y] = '#'

                    nx -= 1


                if cctv4[i] == 2:
                    ny = y - 1
                    while True:
                        if ny < 0:
                            break

                        if cctv_map[x][ny] == 6:
                            break

                        if cctv_map[x][ny] == 0:
                            cctv_map[x][ny] = '#'

                        ny -= 1
                else:
                    ny = y + 1
                    while True:
                        if ny >= m:
                            break

                        if cctv_map[x][ny] == 6:
                            break

                        if cctv_map[x][ny] == 0:
                            cctv_map[x][ny] = '#'

                        ny += 1

            if len(cctv_list) != 0:
                cctv_check(cctv_map, cctv_list)
            else:
                count_zero = 0
                for cctv_line in cctv_map:
                    count_zero += cctv_line.count(0)

                if count_zero < ans:
                    ans = count_zero

            cctv_map[:] = cctv_map_tmp

        cctv_list.insert(0, [x, y, cctv_num])
    elif cctv_num == 5:
        cctv_map_tmp = []
        cctv_map_tmp[:] = [item[:] for item in cctv_map]

        nx = x + 1
        while True:
            if nx >= n:
                break

            if cctv_map[nx][y] == 6:
                break

            if cctv_map[nx][y] == 0:
                cctv_map[nx][y] = '#'

            nx += 1

        nx = x - 1
        while True:
            if nx < 0:
                break

            if cctv_map[nx][y] == 6:
                break

            if cctv_map[nx][y] == 0:
                cctv_map[nx][y] = '#'

            nx -= 1

        ny = y - 1
        while True:
            if ny < 0:
                break

            if cctv_map[x][ny] == 6:
                break

            if cctv_map[x][ny] == 0:
                cctv_map[x][ny] = '#'

            ny -= 1

        ny = y + 1
        while True:
            if ny >= m:
                break

            if cctv_map[x][ny] == 6:
                break

            if cctv_map[x][ny] == 0:
                cctv_map[x][ny] = '#'

            ny += 1

        if len(cctv_list) != 0:
            cctv_check(cctv_map, cctv_list)
        else:
            count_zero = 0
            for cctv_line in cctv_map:
                count_zero += cctv_line.count(0)

            if count_zero < ans:
                ans = count_zero

        cctv_map[:] = cctv_map_tmp

cctv_list = list()
for i in range(n):
    for j in range(m):
        if cctv_map[i][j] != 6 and cctv_map[i][j] != 0:
            cctv_list.append((i, j, cctv_map[i][j]))

cctv_check(cctv_map, cctv_list)
print(ans)
