from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
scores = []
min_score = 51

while True:
    a, b = map(int, input().split())

    if a == - 1 and b == -1:
        break

    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    queue = deque()
    visited = [False] * (n + 1)

    visited[i] = True
    queue.append(i)

    score = 0
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()

            for k in graph[x]:
                if not visited[k]:
                    queue.append(k)
                    visited[k] = True
        score += 1

    score -= 1
    if score < min_score:
        min_score = score
    scores.append((i, score))

ans = []
scores.sort(key=lambda x: x[0])
for member, score in scores:
    if score == min_score:
        ans.append(member)

print(min_score, len(ans))
print(*ans)
