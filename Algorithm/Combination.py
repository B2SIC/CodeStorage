def combination(arr, visited, start, depth, r):
    if depth == r:
        for i in range(len(arr)):
            if visited[i]:
                print(arr[i], end=' ')
        print()
        return

    for i in range(start, len(arr)):
        if not visited[i]:
            visited[i] = True
            combination(arr, visited, i + 1, depth + 1, r)
            visited[i] = False


def combination_allowed_duplication(arr, p, start, depth, r):
    if depth == r:
        print(*p)
        return

    for i in range(start, len(arr)):
        p[depth] = arr[i]
        combination_allowed_duplication(arr, p, i, depth + 1, r)

arr = [1, 2, 3, 4]
r = 2
visited = [False] * len(arr)
p = [0] * r

print("일반 조합")
combination(arr, visited, 0, 0, r)
print("중복 조합")
combination_allowed_duplication(arr, p, 0, 0, r)