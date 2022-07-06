import sys

t = int(input())
result = list()

for i in range(t):
  n = int(input())
  score_list = list()
  for j in range(n):
    score_list.append(list(map(int, sys.stdin.readline().split())))

  score_list.sort(key=lambda x:x[0])

  min_score = score_list[0][1]
  for score in score_list[1:]:
    if score[1] > min_score:
      n -= 1
    else:
      min_score = score[1]

  result.append(n)

for res in result:
  print(res)
