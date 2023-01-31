# 보통의 그리디 문제는 정렬과 관련이 있다.
n = int(input())

time_table = []
for _ in range(n):
    st, ed = map(int, input().split())
    time_table.append([st, ed])

time_table.sort(key=lambda x:x[1])

ans = 0
end = 0
for time in time_table:
    if end <= time[0]:
        ans += 1
        end = time[1]
print(ans)
