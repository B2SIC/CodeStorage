import sys

input = sys.stdin.readline


def binary_search(num_list, target):
    st = 0
    en = len(num_list) - 1

    while st <= en:
        m = (st + en) // 2

        if num_list[m] < target:
            st = m + 1
        elif num_list[m] > target:
            en = m - 1
        else:
            return m
    return -1


n = int(input().rstrip())

num_list = []
for _ in range(n):
    num_list.append(int(input().rstrip()))
num_list.sort()

two = []
for i in range(n):
    for j in range(n):
        two.append(num_list[i] + num_list[j])

two = list(set(two))
two.sort()


def find_ans():
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            idx = binary_search(two, num_list[i] - num_list[j])

            if idx != -1:
                return num_list[i]


print(find_ans())
