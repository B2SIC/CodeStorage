p, m = map(int, input().split())

room_no = 1
room = dict()
for _ in range(p):
    l, n = input().split()
    l = int(l)

    for lev in sorted(room.keys()):
        # 정원 초과
        if len(room[lev]) == m:
            continue
        # 레벨 +- 10 까지 입장 가능
        if room[lev][0][0] - 10 <= l and l <= room[lev][0][0] + 10:
            room[lev].append((l, n))
            break
    else:
        room[room_no] = [(l, n)]
        room_no += 1

for lev in sorted(room.keys()):
    if len(room[lev]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for p_l, p_n in sorted(room[lev], key=lambda x: x[1]):
        print(p_l, p_n)
