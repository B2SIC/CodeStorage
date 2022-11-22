def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

n, m = map(int, input().split())
gcd = gcd(n, m)
print(gcd)
print(n * m // gcd)
