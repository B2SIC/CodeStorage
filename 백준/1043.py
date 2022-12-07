'''
1043번 거짓말

그래프를 이용하여 포함 여부를 판단하여 해결
'''

from collections import deque
import sys


input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
true_man = list(map(int, input().rstrip().split()))

parties = []
for _ in range(m):
    parties.append(list(map(int, input().rstrip().split()))[1:])

if len(true_man) == 1:
    print(m)
else:
    ans = 0
    graph = [[] for _ in range(n + 1)]
    true_man = set(true_man[1:])

    for party in parties:
        for i in range(len(party) - 1):
            graph[party[i]].append(party[i + 1])
            graph[party[i + 1]].append(party[i])

    for i in range(1, n + 1):
        if i in true_man:
            queue = deque()
            queue.append(i)

            while queue:
                x = queue.popleft()

                for k in graph[x]:
                    if k not in true_man:
                        true_man.add(k)
                        queue.append(k)

    for party in parties:
        if len(set(party) & true_man) == 0:
            ans += 1

    print(ans)
