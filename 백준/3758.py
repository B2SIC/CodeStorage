T = int(input())

for _ in range(T):
    # 팀의 개수, 문제의 개수, 나의 팀 ID, 로그 엔트리 개수
    n, k, t, m = map(int, input().split())

    # board = [팀 번호, 총 획득점수, 제출 횟수, 마지막 제출 시간]
    board = [[i, -1, 0, 0] for i in range(n + 1)]
    scores = [[0] * (k + 1) for _ in range(n + 1)]
    cur_time = 1
    for _ in range(m):
        # 팀 ID, 문제 번호, 획득 점수
        i, j, s = map(int, input().split())

        # 획득 점수 및 제출 시간 갱신
        scores[i][j] = max(scores[i][j], s)
        board[i][2] += 1
        board[i][3] = cur_time

        cur_time += 1

    for i in range(1, n + 1):
        board[i][1] = sum(scores[i])

    board.sort(key=lambda x: (-x[1], x[2], x[3]))

    for i in range(n + 1):
        if board[i][0] == t:
            print(i + 1)
