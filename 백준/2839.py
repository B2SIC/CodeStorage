n = int(input())

result = 0

if n % 5 == 0:
    print(n // 5)
else:
    while n != 0:
        if n % 5 == 0:
            n -= 5
            result += 1
        else:
            if n < 3:
                result = -1
                break
            else:
                n -= 3
                result += 1
    print(result)
