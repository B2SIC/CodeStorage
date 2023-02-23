# 삽입정렬 시간 복잡도: O(N^2)
# 단, 어느정도 정렬된 상태라면 빠르게 동작할 수 있다.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i - 1, -1, -1):
        if arr[j + 1] < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
        else:
            break

print(arr)
