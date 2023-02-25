from collections import defaultdict
import sys
input = sys.stdin.readline


n, m = map(int, input().rstrip().split())
words = defaultdict(int)
for _ in range(n):
    get_word = input().rstrip()

    if len(get_word) < m:
        continue

    words[get_word] += 1

sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for key, value in sorted_words:
    print(key)
