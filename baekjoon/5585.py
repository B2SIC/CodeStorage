n = int(input())

change_money = 1000 - n
result = 0

change_list = [500, 100, 50, 10, 5, 1]

for money in change_list:
  result += change_money // money
  change_money = change_money % money

print(result)
