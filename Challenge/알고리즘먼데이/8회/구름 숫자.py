# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
groom = input()

groom_dict = {
    'qw': '1', 'as': '2', 'zx': '3',
    'we': '4', 'sd': '5', 'xc': '6',
    'er': '7', 'df': '8', 'cv': '9', 'ze': '0'
}

ans = ''
for i in range(len(groom) - 1):
    concat = groom[i] + groom[i + 1]

    if concat in groom_dict.keys():
        ans += groom_dict[concat]

print(ans)
