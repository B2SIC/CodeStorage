n = int(input())

for _ in range(n):
    stack = list()

    get_ps = list(input())

    result = ""
    for ps in get_ps:
        if ps == '(':
            stack.append(ps)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                result = "NO"
                break

    if result == "":
        if len(stack) > 0:
            result = "NO"
        else:
            result = "YES"

    print(result)
