n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

result = []

i, j = 0, 0
while i < n and j < m:
    if n_list[i] <= m_list[j]:
        result.append(n_list[i])
        i += 1
    else:
        result.append(m_list[j])
        j += 1

if i < n:
    while i < n:
        result.append(n_list[i])
        i += 1
elif j < m:
    while j < m:
        result.append(m_list[j])
        j += 1

print(*result)
