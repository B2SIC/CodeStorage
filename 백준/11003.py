# Unsolved

from collections import deque
import sys

input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
num_list = list(map(int, input().rstrip().split()))

queue = deque()
min_num = int(1e18)
count = 0
for num in num_list:
    if num < min_num:
        min_num = num

    if count < l:
        queue.append(num)
        count += 1
    else:
        val = queue.popleft()
        queue.append(num)
        if val == min_num:
            min_num = min(queue)

    print(min_num, end=' ')
