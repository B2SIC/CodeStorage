def dfs(start, sum_of_nums):
    # CUT-EDGE -> 합이 같으려면 전체 합의 절반을 넘기면 안된다.
    if sum_of_nums > total // 2:
        return
    if start == n:
        if sum_of_nums == total - sum_of_nums:
            global res
            res = True
        return

    dfs(start + 1, sum_of_nums + arr[start])
    dfs(start + 1, sum_of_nums)

n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
res = False
dfs(0, 0)

if res:
    print("YES")
else:
    print("NO")
