from collections import defaultdict
import sys


input = sys.stdin.readline

m, n = map(int, input().rstrip().split())

spaces = []
for _ in range(m):
    planet_list = list(map(int, input().rstrip().split()))

    for i in range(len(planet_list)):
        planet_list[i] = (i, planet_list[i])

    planet_list.sort(key=lambda x:x[1])
    spaces.append(planet_list)

space_dict = defaultdict(int)
dup_check = []
for space in spaces:
    idx = ''
    num_list = []
    for elem in space:
        idx += str(elem[0])
        num_list.append(elem[1])
    for i in range(len(space) - 1):
        if space[i][1] < space[i + 1][1]:
            idx += '<'
        elif space[i][1] == space[i + 1][1]:
            idx += '='

    if num_list not in dup_check:
        dup_check.append(num_list)
        space_dict[idx] += 1

ans = 0
for value in space_dict.values():
    ans += (value * (value - 1)) // 2

print(ans)
