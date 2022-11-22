n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def backTracking(k, sum):
  global ans
  if k == n:
    if sum == s:
      ans += 1
    return

  backTracking(k + 1, sum)
  backTracking(k + 1, sum + arr[k])

backTracking(0, 0)

if s == 0:
  ans -= 1
print(ans)
