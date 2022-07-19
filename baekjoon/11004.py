n, k = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()
print(a_list[k - 1])
