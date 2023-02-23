def spare_after_cut(heights, size):
    res = 0
    for height in heights:
        if size < height:
            res += (height - size)
    return res


n, m = map(int, input().split())
ddok_heights = list(map(int, input().split()))
ddok_heights.sort()
start = 0
end = max(ddok_heights)
ans = 0
while start <= end:
    mid = (start + end) // 2

    result = spare_after_cut(ddok_heights, mid)
    if result >= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
