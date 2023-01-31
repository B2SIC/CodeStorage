n = 9
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def sudoku_validator(graph):
    # 행, 열 검사
    for i in range(n):
        check_number = []
        for num in graph[i]:
            if num in check_number:
                return False
            check_number.append(num)

        check_number = []
        for j in range(n):
            if graph[j][i] in check_number:
                return False
            check_number.append(graph[j][i])

    # 3 X 3 검사
    dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            check_number = []
            for k in range(9):
                if graph[i + dx[k]][j +dy[k]] in check_number:
                    return False
                check_number.append(graph[i + dx[k]][j +dy[k]])
    return True


if sudoku_validator(graph):
    print("YES")
else:
    print("NO")
