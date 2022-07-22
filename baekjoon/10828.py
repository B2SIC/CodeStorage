import sys

n = int(input())

stack = list()
for _ in range(n):
  get_command = list(sys.stdin.readline().rstrip().split())

  command = get_command[0]

  if command == 'push':
    stack.append(get_command[1])
  elif command == 'pop':
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
  elif command == 'size':
    print(len(stack))
  elif command == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif command == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
