# import sys
#
# sys.stdin = open('in1.txt', 'rt')

n, k = map(int, input().split())
num_list = list(map(int, input().split()))

result = set()
for i in range(n):
    for j in range(i + 1, n):
        for l in range(j + 1, n):
            result.add(num_list[i] + num_list[j] + num_list[l])

result = list(result)
result.sort(reverse=True)
print(result[k - 1])
