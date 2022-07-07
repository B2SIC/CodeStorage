n, k = map(int, input().split())

josephus_list = [i for i in range(1, n + 1)]
idx = 0
popped_list = list()

while josephus_list:
  if idx == k - 1:
    idx %= len(josephus_list)
    josephus_list += josephus_list[:idx]
    del josephus_list[:idx]
    popped_list.append(josephus_list.pop(0))
    idx = 0
  else:
      idx += 1

print("<" + ", ".join(map(str, popped_list)) + ">")
