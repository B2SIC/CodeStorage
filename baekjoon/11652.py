import sys

n = int(input())

card_dict = dict()

for _ in range(n):
  card_num = int(sys.stdin.readline().rstrip())

  if card_dict.get(card_num, -1) == -1:
    card_dict[card_num] = 1
  else:
    card_dict[card_num] += 1

max_key = 0
max_value = 0
for key, value in sorted(card_dict.items(), key=lambda x: (-x[1], x[0])):
  if value > max_value:
    max_key = key
    max_value = value

print(max_key)
