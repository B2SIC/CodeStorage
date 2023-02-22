import sys
input = sys.stdin.readline

m = int(input().rstrip())
S = set()
for _ in range(m):
    commands = input().rstrip().split()
    command = commands[0]

    if len(commands) > 1:
        commands[1] = int(commands[1])

    if command == "add":
        S.add(commands[1])
    elif command == "remove":
        S.discard(commands[1])
    elif command == "check":
        if commands[1] in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if commands[1] in S:
            S.remove(commands[1])
        else:
            S.add(commands[1])
    elif command == "empty":
        S.clear()
    elif command == "all":
        S = {i for i in range(1, 21)}
