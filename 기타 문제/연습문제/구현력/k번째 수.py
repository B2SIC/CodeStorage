# import sys
#
# sys.stdin = open('in4.txt', 'rt')
t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    print(f"#{i + 1} {sorted(num_list[s - 1:e])[k - 1]}")
