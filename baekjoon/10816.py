n = int(input())

my_card_list = list(map(int, input().split()))

m = int(input())
your_card_list = list(map(int, input().split()))

card_dict = dict()

for card in my_card_list:
  if card_dict.get(card, -1) == -1:
    card_dict[card] = 1
  else:
    card_dict[card] += 1

for card in your_card_list:
  if card_dict.get(card, -1) == -1:
    print(0, end=' ')
  else:
    print(card_dict[card], end=' ')
