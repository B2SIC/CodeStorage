def is_valid(road, n, L):
    valid = True
    before = 0
    cur = 0
    visited = [0] * n

    while valid and cur < n:
        if before == cur:
            cur += 1
        else:
            # 이전 값과 현재 값 비교 후 같다면 이전 값을 현재 값으로 변경
            if road[before] == road[cur]:
                before += 1
                cur += 1
            else:
                # 값이 다르다면 높이 차이가 1인지 확인
                if abs(road[before] - road[cur]) == 1:
                    # L만큼 경사로를 깔 수 있는지 체크
                    stand = 0  # 기준 값
                    offset = 0  # 경사로 확인 오프셋 +1 or -1
                    check_idx = -1  # 현재 체크 값
                    if road[before] < road[cur]:  # 더 높은 경사로 -> 앞 쪽 값 확인 필요
                        stand = cur
                        check_idx = cur
                        offset = -1
                    else:  # 낮은 경사로 -> 뒤 쪽 값 확인 필요
                        stand = before
                        check_idx = before
                        offset = 1

                    for _ in range(L):
                        nx_idx = check_idx + offset

                        # 범위를 벗어난 경우
                        if nx_idx < 0 or nx_idx >= n:
                            valid = False
                            break

                        # 이미 경사로를 깔았거나 높이가 기준과 다르다면 -> 경사로 설치 불가능
                        if not visited[nx_idx] and abs(road[nx_idx] - road[stand]) == 1:
                            visited[nx_idx] = 1
                            check_idx = nx_idx
                        else:
                            valid = False
                            break

                    # 경사로를 깔고 나서 값 세팅
                    if valid:
                        if road[before] < road[cur]:
                            before = cur
                        else:
                            before = check_idx
                            cur = check_idx
                else:  # 값이 다른데 높이 차가 1이 아니면 -> 갈 수 없는 길
                    valid = False

    return valid


n, L = map(int, input().split())
maps = []
case = []  # 검사 대상인 길 목록
# 값을 받아오면서 행에 대한 케이스 저장
for _ in range(n):
    row = list(map(int, input().split()))
    maps.append(row)
    case.append(row)

# 열 기준 길 목록을 검사 대상에 추가
for i in range(n):
    columns = []
    for j in range(n):
        columns.append(maps[j][i])
    case.append(columns)

res = 0
for elem in case:
    if is_valid(elem, n, L):
        res += 1

print(res)
