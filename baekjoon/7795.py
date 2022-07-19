t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_list.sort(reverse=True)
    b_list.sort(reverse=True)
    result = 0
    for i in range(len(a_list)):
        if a_list[i] > b_list[0]:
            result += len(b_list)
        elif a_list[i] <= b_list[-1]:
            break
        else:
            for j in range(len(b_list)):
                if a_list[i] > b_list[j]:
                    result += len(b_list) - j
                    break

    print(result)
