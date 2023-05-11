def solution(n):
    if n >= 1 and n <= 99:
        return True

    arr = []
    while n > 0:
        arr.append(n % 10)
        n = n // 10

    diff = arr[0] - arr[1]
    for i in range(1, len(arr) - 1):
        if arr[i] - arr[i + 1] != diff:
            return False
    return True


n = int(input())
res = 0
for i in range(1, n + 1):
    if solution(i):
        res += 1
print(res)
