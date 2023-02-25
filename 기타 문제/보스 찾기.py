'''
S사 코딩테스트 기출 문제
'''
from collections import defaultdict


ans = []
check_member = list(map(int, input().split()))  # [4, 5]
arr = [2, 2, -1, 1, 5, -1, 5]
group_map = defaultdict(list)

def find_parent(parent, x):
    if parent[x] != -1:
        return find_parent(parent, parent[x])
    return x

for i in range(len(arr)):
    group_map[find_parent(arr, i)].append(i)

for member in check_member:
    if member in group_map.keys():
        ans.append(1)
    else:
        ans.append(0)

print(ans)
