n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

sum = 0

for i in range(n):
  sum += a_list[i] * b_list[i]

print(sum)
