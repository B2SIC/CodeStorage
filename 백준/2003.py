n, m = map(int, input().split())

num_list = list(map(int, input().split()))

for i in range(1, len(num_list)):
    num_list[i] += num_list[i - 1]

res = 0
for i in range(len(num_list)):
    if num_list[i] == m:
        res += 1
    elif num_list[i] > m:
        for j in range(i - 1, -1, -1):
            diff = num_list[i] - num_list[j]
            if diff >= m:
                if diff == m: res += 1
                break

print(res)
