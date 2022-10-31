n, m = map(int, input().split())

arr = [0] * m
is_used = [False] * (n + 1)

def backTracking(k):
  if k == m:
    print(*arr)
    return

  for i in range(1, n + 1):
    if is_used[i] is False:
      arr[k] = i
      is_used[i] = True
      backTracking(k + 1)
      is_used[i] = False

backTracking(0)
