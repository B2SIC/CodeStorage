'''
13414번 수강신청

해시를 이용한 대기열 구현
'''

import sys


input = sys.stdin.readline

k, l = map(int, input().rstrip().split())

queue = {input().rstrip(): i for i in range(1, l + 1)}
queue = sorted(queue.items(), key=lambda x: x[1])
queue_size = len(queue)

for i in range(k):
    if i >= queue_size:
        break
    print(queue[i][0])
