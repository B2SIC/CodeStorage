from collections import deque

def solution(maps):
    # 오른쪽 -> 왼쪽 -> 위 -> 아래
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    r = len(maps)  # y 최대 길이
    c = len(maps[0])  # x 최대 길이

    graph = [[-1 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        y, x = queue.popleft()  # 리스트에서 뽑은 값은 (y, x) 순이다.

        # 현재 위치에서 direction 순서에 따른 위치 확인
        for i in range(4):
            # 다음 위치 계산
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if 0 <= nx < c and 0 <= ny < r and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    answer = graph[-1][-1]
    return answer

result = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
print(result)
