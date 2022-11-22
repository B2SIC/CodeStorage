a, b = map(int, input().split())
answer = 0

while b > a:
  if b % 2 == 0:
    b /= 2
    b = int(b)
    answer += 1
  else:
    if b >= 11:
      if str(b)[-1] == '1':
        b = int(str(b)[:-1])
        answer += 1
      else:
        break
    else:
      break

if a == b:
  print(answer + 1)
else:
  print(-1)
