n = int(input())

arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))

arr_dict = dict()
num_count = 0

for num in sorted_arr:
  if arr_dict.get(num, -1) == -1:
    arr_dict[num] = num_count
    num_count += 1

for num in arr:
  print(arr_dict[num], end=' ')
