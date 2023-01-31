# m이 크면 시간초과가 발생할 우려가 있음.

L = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()

for _ in range(m):
    arr[0] += 1
    arr[-1] -= 1
    arr.sort()

print(arr[-1] - arr[0])