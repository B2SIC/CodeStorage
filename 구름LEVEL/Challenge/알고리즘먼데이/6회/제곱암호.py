# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def decoding(s):
    plain_text = ''
    for i in range(0, len(s), 2):
        asc_num = ord(s[i])
        asc_num += int(s[i + 1]) ** 2

        while asc_num > 122:
            asc_num -= 26

        plain_text += chr(asc_num)

    return plain_text


n = int(input())
print(decoding(input()))