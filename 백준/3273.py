n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()
start = 0
end = len(array) - 1

result = 0
while start < end:
  if x < end:
    end -= 1
  else:
    if array[start] + array[end] == x:
      result += 1
      start += 1
      end -= 1
    elif array[start] + array[end] < x:
      start += 1
    elif array[start] + array[end] > x:
      end -= 1

print(result)
