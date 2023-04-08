# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, m = map(int, input().split())
pay_waiting_list = []

for _ in range(m):
    order, value = input().split()
    value = int(value)

    if order == "deposit":
        n += value

        while len(pay_waiting_list) > 0 and n >= pay_waiting_list[0]:
            n -= pay_waiting_list.pop(0)
    elif order == "pay":
        if n >= value:
            n -= value
    elif order == "reservation":
        if n < value or len(pay_waiting_list) >= 1:
            pay_waiting_list.append(value)
        else:
            n -= value

print(n)
