S = input()

zero = S.count('0') // 2
one = S.count('1') // 2

new_S = ""
for elem in S:
    if elem == '0':
        if zero <= 0:
            continue
        else:
            new_S += elem
            zero -= 1
    else:
        if one <= 0:
            new_S += elem
        else:
            one -= 1

print(new_S)
