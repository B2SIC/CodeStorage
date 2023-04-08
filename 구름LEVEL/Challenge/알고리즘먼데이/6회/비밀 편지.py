# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline


def tokenizer(s, token):
    iter_token = token
    if len(s) != len(token):
        if len(s) % len(token) == 0:
            token = iter_token * (len(s) // len(token))
        else:
            token += iter_token * (len(s) // len(token))
    return token


def encoding(s, token):
    decorded_text = ''
    token = tokenizer(s, token)

    for i in range(len(s)):
        standard = ord(s[i])
        token_ascii = ord(token[i])

        end = 0
        if standard >= 65 and standard <= 90:
            end = 90
        elif standard >= 97 and standard <= 122:
            end = 122

        if end == 0:
            decorded_text += s[i]
        else:
            enc_ascii = standard + token_ascii
            while enc_ascii > end:
                enc_ascii -= 26
            decorded_text += chr(enc_ascii)

    return decorded_text


def decoding(s, token):
    plain_text = ''
    token = tokenizer(s, token)

    for i in range(len(s)):
        standard = ord(s[i])
        token_ascii = ord(token[i])

        end = 0
        if standard >= 65 and standard <= 90:
            end = 65
        elif standard >= 97 and standard <= 122:
            end = 97

        if end == 0:
            plain_text += s[i]
        else:
            dec_ascii = standard - token_ascii
            while dec_ascii < end:
                dec_ascii += 26
            plain_text += chr(dec_ascii)

    return plain_text


for _ in range(int(input())):
    get_text = input().rstrip()
    order, token = input().rstrip().split()

    if order == 'E':
        print(encoding(get_text, token))
    elif order == 'D':
        print(decoding(get_text, token))
