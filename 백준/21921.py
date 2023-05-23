N, X = map(int, input().split())
visit_count = list(map(int, input().split()))

cur_visit = sum(visit_count[:X])
max_visit = sum(visit_count[:X])
count = 1
for i in range(0, N - X):
    cur_visit = cur_visit - visit_count[i] + visit_count[i + X]
    if cur_visit > max_visit:
        max_visit = cur_visit
        count = 1
    elif cur_visit == max_visit:
        count += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(count)
