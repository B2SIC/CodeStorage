n = int(input())

new_n = 0
num = 1
count = 0
while True:
    if new_n == n:
        break
    else:
        if new_n + num <= n:
            new_n += num
            num += 1
            count += 1
        else:
            break

print(count)
