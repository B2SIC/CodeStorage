n, m = map(int, input().split())

video_times = list(map(int, input().split()))

start = max(video_times)
end = sum(video_times)
result = 0

while start <= end:
    mid = (start + end) // 2

    count = 1
    video_time = 0
    for video in video_times:
        if video_time + video > mid:
            count += 1
            video_time = video
        else:
            video_time += video

    if count <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
