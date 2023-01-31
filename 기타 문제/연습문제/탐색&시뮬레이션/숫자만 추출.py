s = input()

num = 0
for chr in s:
    if chr.isdecimal():  # 0 ~ 9 까지의 숫자만 True
        num = num * 10 + int(chr)

ans = 0
for i in range(1, num + 1):
    if num % i == 0:
        ans += 1

print(num)
print(ans)
