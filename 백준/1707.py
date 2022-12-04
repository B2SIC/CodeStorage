'''
1707번 이분 그래프

인접한 노드끼리는 다른 색, 같은 레벨에 존재하는 노드끼리는 같은 색으로 칠해지면
이분 그래프, 아니면 이분 그래프가 아님
'''

from collections import deque
import sys

input = sys.stdin.readline
is_bipar_graph = True


def bfs(v, graph, colors):
    global is_bipar_graph
    colors[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if colors[i] == 0:
                queue.append(i)
                colors[i] = colors[x] * (-1)
            else:
                if colors[x] == colors[i]:
                    is_bipar_graph = False
                    return


for _ in range(int(input())):
    v, e = map(int, input().rstrip().split())

    graph = [[] for _ in range(v + 1)]
    colors = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().rstrip().split())

        graph[a].append(b)
        graph[b].append(a)

    is_bipar_graph = True
    for i in range(1, v + 1):
        if colors[i] == 0:
            bfs(i, graph, colors)

        if not is_bipar_graph:
            break

    if is_bipar_graph:
        print("YES")
    else:
        print("NO")
