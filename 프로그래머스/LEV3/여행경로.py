from collections import defaultdict

answer = []


def dfs(airports, cur):
    global answer

    while airports[cur]:
        nx = airports[cur].pop()
        dfs(airports, nx)

    if not airports[cur]:
        answer.append(cur)
        return


def solution(tickets):
    airports = defaultdict(list)
    for start, end in tickets:
        airports[start].append(end)
    for key in airports.keys():
        airports[key].sort(reverse=True)

    start = "ICN"
    dfs(airports, start)

    return answer[::-1]

solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])
