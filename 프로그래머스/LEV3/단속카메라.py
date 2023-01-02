def solution(routes):
    stack = []
    routes.sort(key=lambda x: x[0])

    for st, ed in routes:
        if not stack:
            stack.append((st, ed))
        else:
            top_st, top_ed = stack[-1]
            is_combine = (max(top_st, st), min(top_ed, ed))

            if is_combine[0] <= is_combine[1]:
                stack.pop()
                stack.append(is_combine)
            else:
                stack.append((st, ed))

    return len(stack)
