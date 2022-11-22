def factorial(num: int):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

get_num = int(input())
result = factorial(get_num)
print(result)
