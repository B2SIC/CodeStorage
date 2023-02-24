import sys
input = sys.stdin.readline

s = input().rstrip()
half = len(s) // 2
s1 = list(map(int, s[:half]))
s2 = list(map(int, s[half:]))

if sum(s1) == sum(s2):
    print("LUCKY")
else:
    print("READY")
