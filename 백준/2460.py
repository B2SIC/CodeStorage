ans = 0
cur_person = 0
for _ in range(10):
    out, get_in = map(int, input().split())

    cur_person += get_in - out
    if ans < cur_person:
        ans = cur_person

print(ans)
