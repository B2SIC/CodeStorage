'''
계수 정렬 시간복잡도: O(N + K)
계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
데이터의 최대 값과 최소값의 차이가 1,000,000 이하이며 중복이 많을 때 효과적임
이유는 모든 데이터의 범위를 담을 수 있는 리스트(배열)를 선언하여 사용하기 때문이다.
이 때문에 특정 상황에서는 극단적으로 비효율적일 수 있음. ex) [1, 999,999]
'''
arr = [7, 5, 3, 9, 0, 3, 1, 6, 2, 4, 8, 8]
count_sort = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count_sort[arr[i]] += 1

for i in range(len(count_sort)):
    for j in range(count_sort[i]):
        print(i, end=' ')
