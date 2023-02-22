import sys
input = sys.stdin.readline

n, game = input().rstrip().split()
n = int(n)

already_done = set()  # 플레이 한 유저 목록
player_list = []  # 전체 플레이 신청 유저 목록
play_time = 0  # 플레이 횟수
for _ in range(n):
    player_list.append(input().rstrip())

max_player = 0
if game == 'Y':
    max_player = 2
elif game == 'F':
    max_player = 3
elif game == 'O':
    max_player = 4

cur_player = 1
for player in player_list:
    if player in already_done:  # O(1)
        continue

    already_done.add(player)
    cur_player += 1

    if cur_player == max_player:
        play_time += 1
        cur_player = 1

print(play_time)
