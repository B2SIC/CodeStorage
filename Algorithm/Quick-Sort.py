'''
퀵정렬 시간 복잡도: 평균 O(NlogN), 최악 O(N^2)
데이터가 정렬되어 있을 경우 매우 느리게 동작한다. (삽입 정렬과 반대)
C++의 퀵 정렬은 피벗값 설정에 추가 로직을 더해줘서 최악의 경우에도 O(NlogN)을 보장해준다.
파이썬의 sorted 함수는 퀵정렬과 비슷한 병합정렬과 삽입 정렬의 아이디어를 기반으로 하이브리드 방식으로 만들어짐.
병합정렬은 일반적으로 퀵정렬보다 느리나, 최악의 경우에도 시간 복잡도 O(NlogN)을 보장해준다.
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 전통적인 방식의 퀵 정렬
def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

# Pythonic 한 방법
def quick_sort_pythonic(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_pythonic(left_side) + [pivot] + quick_sort_pythonic(right_side)

# quick_sort(arr, 0, len(arr) - 1)
print(quick_sort_pythonic(arr))
