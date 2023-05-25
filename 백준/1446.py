from collections import deque


def dfs(depth, p):
    if depth == len(p):
        path = deque()
        for i in range(len(p)):
            if p[i]:
                path.append(short_path[i])

        cur_pos = 0
        distance = 0
        while path:
            # 현재 위치가 D보다 크거나 같다면 종료
            if cur_pos >= D:
                break

            s, e, dis = path.popleft()
            if cur_pos > s:
                continue

            # 지름길까지 이동
            distance += s - cur_pos

            # 지름길 타기
            cur_pos = e
            distance += dis

        # 남은 거리 이동
        if cur_pos < D:
            distance += (D - cur_pos)
            cur_pos = D

        global min_dis
        min_dis = min(min_dis, distance)
        return

    p[depth] = 0
    dfs(depth + 1, p)
    p[depth] = 1
    dfs(depth + 1, p)


N, D = map(int, input().split())
get_path = []
for _ in range(N):
    get_path.append(list(map(int, input().split())))

# 진짜 지름길 선별 및 정렬
short_path = []
for path in get_path:
    if path[1] > D:
        continue
    if path[1] - path[0] > path[2]:
        short_path.append(path)
short_path.sort(key=lambda x: x[0])

min_dis = D
p = [0] * len(short_path)  # 케이스
dfs(0, p)

print(min_dis)
