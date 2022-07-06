n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()

sum = p_list[0]
part_sum = p_list[0]
for i in range(len(p_list) - 1):
  part_sum += p_list[i + 1]
  sum += part_sum

print(sum)