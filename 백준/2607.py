import string
import copy

n = int(input())
rep_word = input()

word_list = []
for _ in range(n - 1):
    word_list.append(input())

base_dict = {alpha: 0 for alpha in string.ascii_uppercase}
rep_dict = copy.deepcopy(base_dict)

for elem in rep_word:
    rep_dict[elem] += 1

ans = 0
for word in word_list:
    if abs(len(rep_word) - len(word)) > 1:
        continue

    word_dict = copy.deepcopy(base_dict)
    for elem in word:
        word_dict[elem] += 1

    diff = 0
    for alpha in string.ascii_uppercase:
        diff += abs(rep_dict[alpha] - word_dict[alpha])

    if diff <= 2:
        ans += 1

print(ans)
