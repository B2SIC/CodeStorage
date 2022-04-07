n, m = map(int, input().split())
card_list = list(map(int, input().split()))
sum_list = list()
off_set_list = list()

for i in range(len(card_list)):
    for j in range(i+1, len(card_list)):
        for k in range(j+1, len(card_list)):
            sum_list.append(card_list[i] + card_list[j] +card_list[k])

for sum in sum_list:
    off_set_list.append(m - sum)

index = -1
min = 99999
for i, data in enumerate(off_set_list):
    if data < 0:
        continue

    if data < min:
        min = data
        index = i

print(sum_list[index])