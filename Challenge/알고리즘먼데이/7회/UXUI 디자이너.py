# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import defaultdict

n, m = map(int, input().split())
event = defaultdict(int)
for _ in range(m):
    events = list(map(int, input().split()))

    for ev in events[1:]:
        event[ev] += 1

sorted_event = sorted(event.items(), key=lambda x: x[1], reverse=True)
max_time = sorted_event[0]
ans = []

for key, value in sorted_event:
    if value == max_time[1]:
        ans.append(key)

print(*sorted(ans, reverse=True))