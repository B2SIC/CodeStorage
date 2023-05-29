import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

word_dict = dict()
for _ in range(n):
    word_dict[input().rstrip()] = 1

for _ in range(m):
    words = input().rstrip().split(',')

    for word in words:
        if word in word_dict:
            word_dict.pop(word)

    print(len(word_dict))
