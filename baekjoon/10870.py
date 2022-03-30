def fibo(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

get_num = int(input())
result = fibo(get_num)
print(result)
