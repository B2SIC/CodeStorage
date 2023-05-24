N, K = map(int, input().split())
data = list(input())
ans = 0

person_pos = []
for i in range(len(data)):
    if data[i] == 'P':
        person_pos.append(i)

for elem in person_pos:
    for k in range(max(0, elem - K), elem):
        if data[k] == 'H':
            ans += 1
            data[k] = '-'
            break
    else:
        for k in range(elem + 1, min(elem + K + 1, N)):
            if data[k] == 'H':
                ans += 1
                data[k] = '-'
                break
print(ans)
