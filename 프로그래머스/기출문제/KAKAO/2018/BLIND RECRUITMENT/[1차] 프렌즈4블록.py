def find_four_block(m, n, board):
    bomb = set()
    dx = [0, 1, 1]
    dy = [1, 0, 1]

    for x in range(m):
        for y in range(n):
            if board[x][y] != '-':
                block_bomb = True

                for k in range(3):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0 or nx >= m or ny >= n or board[nx][ny] != board[x][y]:
                        block_bomb = False
                        break

                if block_bomb:
                    for k in [(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1)]:
                        bomb.add(k)
    return bomb


def solution(m, n, board):
    answer = 0

    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        bomb = find_four_block(m, n, board)
        if not bomb:
            break
        answer += len(bomb)

        for x, y in bomb:
            board[x][y] = '-'

        for y in range(n):
            for x in range(m - 1, -1, -1):
                if board[x][y] == '-':
                    k = x - 1
                    while k >= 0:
                        if board[k][y] != '-':
                            board[x][y], board[k][y] = board[k][y], board[x][y]
                            break
                        k -= 1
    return answer
