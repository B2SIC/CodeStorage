n, m = map(int, input().split())

wood_length = list(map(int, input().split()))

start = 0
end = max(wood_length)

result = 0
while start <= end:
    mid = (start + end) // 2
    get_wood = 0

    for wood in wood_length:
        if wood > mid:
            get_wood += wood - mid

    if get_wood < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
