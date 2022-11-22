import sys

k, n = map(int, input().split())

line_list = list()
for _ in range(k):
    line_list.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(line_list)
result = 0

while start <= end:
    mid = (start + end) // 2
    num_of_line = 0

    for line in line_list:
        num_of_line += line // mid

    if num_of_line < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
