# DFS 재귀 방식
def dfs_recursive(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if visited[i]: continue
        dfs_recursive(graph, i, visited)


# DFS 비재귀 방식 (스택과 flag 변수를 활용한 방법)
def dfs_stack1(graph, v):
    visited = [False] * 9
    stack = [v]
    visited[v] = True
    print(v, end=' ')

    while stack:
        node = stack[-1]
        flag = False
        for i in graph[node]:
            if visited[i]: continue
            stack.append(i)
            visited[i] = True
            flag = True
            print(i, end=' ')
            break

        if not flag:
            stack.pop()


# DFS 비재귀 방식2 (스택을 이용해서 BFS 처럼 구현)
def dfs_stack2(graph, v):
    visited = [False] * 9
    stack = [v]

    while stack:
        node = stack.pop()

        if visited[node]: continue
        visited[node] = True
        print(node, end=' ')

        for i in graph[node][::-1]:
            if visited[i]: continue
            stack.append(i)


# Node: 1 ~ 8
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

dfs_recursive(graph, 1, visited)
print()
dfs_stack1(graph, 1)
print()
dfs_stack2(graph, 1)
