# 규칙성 발견 -> n이 짝수면 CY 승리, 홀수면 SK가 승리한다.
n = int(input())

if n % 2 == 0:
    print("CY")
else:
    print("SK")
