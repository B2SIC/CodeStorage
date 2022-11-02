import sys

n = int(input())
queue = [0] * 10000
head, tail = 0, 0

for _ in range(n):
  command = sys.stdin.readline().rstrip()

  if "push" in command:
    order, value = command.split()
    queue[tail] = int(value)
    tail += 1
  elif command == "front":
    if head != tail:
      print(queue[head])
    else:
      print(-1)
  elif command == "back":
    if head != tail:
      print(queue[tail - 1])
    else:
      print(-1)
  elif command == "pop":
    if head != tail:
      print(queue[head])
      head += 1
    else:
      print(-1)
  elif command == "size":
    print(tail - head)
  elif command == "empty":
    if head != tail:
      print(0)
    else:
      print(1)
