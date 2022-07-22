from collections import deque
import sys

n = int(input())
queue = deque()

for _ in range(n):
  get_command = list(sys.stdin.readline().rstrip().split())
  command = get_command[0]

  if command == "push":
    queue.append(get_command[1])
  elif command == "front":
    if len(queue) > 0:
      print(queue[0])
    else:
      print(-1)
  elif command == "back":
    if len(queue) > 0:
      print(queue[-1])
    else:
      print(-1)
  elif command == "size":
    print(len(queue))
  elif command == "empty":
    if len(queue) > 0:
      print(0)
    else:
      print(1)
  elif command == "pop":
    if len(queue) > 0:
      print(queue.popleft())
    else:
      print(-1)
