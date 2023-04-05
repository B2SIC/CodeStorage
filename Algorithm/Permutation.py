def permutation(arr, p, visited, depth, r):
    if depth == r:
        print(*p)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            p[depth] = arr[i]
            permutation(arr, p, visited, depth + 1, r)
            visited[i] = False

def permutation_allowed_duplication(arr, p, depth, r):
    if depth == r:
        print(*p)
        return

    for i in range(len(arr)):
        p[depth] = arr[i]
        permutation_allowed_duplication(arr, p, depth + 1, r)

arr = [1, 2, 3, 4]
r = 3
visited = [False] * len(arr)
p = [0] * r

print("일반 순열")
permutation(arr, p, visited, 0, r)
print("중복 순열")
permutation_allowed_duplication(arr, p, 0, r)
