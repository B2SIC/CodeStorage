seq = input()
stack = []

ans = 0
for elem in seq:
    if elem == '(':
        stack.append(elem)
    elif elem == ')':
        if stack[-1] == '(':
            stack.pop()
            stack.append('L')
        else:
            laser = 0
            while stack:
                popped = stack.pop()
                if popped == '(':
                    break
                elif popped == 'L':
                    laser += 1
            ans += (laser + 1)

            for _ in range(laser):
                stack.append('L')

print(ans)
