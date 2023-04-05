# PyPy3 기준 통과

def dfs(depth, p):
    global min_value, max_value
    if depth == n - 1:
        result = nums[0]

        for num, op in zip(nums[1:], p):
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            elif op == '*':
                result *= num
            elif op == '/':
                if result < 0:
                    result = -result
                    result //= num
                    result = -result
                else:
                    result //= num

        if result < min_value:
            min_value = result
        if result > max_value:
            max_value = result
        return

    for i in range(n - 1):
        if not visited[i]:
            visited[i] = 1
            p[depth] = operator[i]
            dfs(depth + 1, p)
            visited[i] = 0


n = int(input())
nums = list(map(int, input().split()))
operator_by_num = list(map(int, input().split()))
operator = []
operator.extend(['+'] * operator_by_num[0])
operator.extend(['-'] * operator_by_num[1])
operator.extend(['*'] * operator_by_num[2])
operator.extend(['/'] * operator_by_num[3])

p = [''] * (n - 1)
visited = [0] * (n - 1)
min_value = int(1e9)
max_value = -int(1e9)
dfs(0, p)

print(max_value)
print(min_value)
