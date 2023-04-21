n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

sum = (m // (k + 1)) * ((nums[0] * k) + nums[1])
sum += (m % (k + 1)) * nums[0]
print(sum)
