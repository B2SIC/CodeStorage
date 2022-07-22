while True:
    get_str = list(input())
    stack = list()

    if len(get_str) == 1 and get_str[0] == '.':
        break
    else:
        result = ""

        for chr in get_str:
            if chr == '(':
                stack.append(chr)
            elif chr == '[':
                stack.append(chr)
            elif chr == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    result = "no"
                    break
            elif chr == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    result = "no"
                    break

        if result == "":
            if len(stack) == 0:
                result = 'yes'
            else:
                result = 'no'

        print(result)
