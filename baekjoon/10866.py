import sys
from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
  get_command = list(sys.stdin.readline().rstrip().split())

  command = get_command[0]

  if command == 'push_front':
    queue.appendleft(get_command[1])
  elif command == 'push_back':
    queue.append(get_command[1])
  elif command == 'pop_front':
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif command == 'pop_back':
    if queue:
      print(queue.pop())
    else:
      print(-1)
  elif command == 'size':
    print(len(queue))
  elif command == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif command == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif command == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)
