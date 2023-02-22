import sys

input = sys.stdin.readline

# n = 리스트 내 점수 개수, score = 태수 점수, p = 최대 랭킹 개수
n, score, p = map(int, input().rstrip().split())
rank = []
is_in_list = True
if n >= 1:
    rank = list(map(int, input().rstrip().split()))
    rank.sort(reverse=True)

for i in range(len(rank)):
    if score > rank[i]:  # 리스트 점수보다 태수 점수가 더 큼
        rank.insert(i, score)
        break
else:
    if p > len(rank):
        rank.append(score)
    else:
        is_in_list = False

if is_in_list:
    rank = rank[:p]

    for i in range(len(rank)):
        if rank[i] == score:
            print(i + 1)
            break
    else:
        print(-1)
else:
    print(-1)
