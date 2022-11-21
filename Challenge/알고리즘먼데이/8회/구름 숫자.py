# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
s = input()

groom_dict = dict()
groom_num = [i for i in range(10)]
groom_str = ['ze', 'qw', 'as', 'zx', 'we', 'sd', 'xc', 'er', 'df', 'cv']

for i in range(10):
    groom_dict[groom_str[i]] = groom_num[i]

for k in range(len(s) - 1):
    comb = s[k] + s[k + 1]

    if groom_dict.get(comb, -1) == -1:
        continue

    print(groom_dict[comb], end='')
