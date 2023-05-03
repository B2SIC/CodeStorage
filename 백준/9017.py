from collections import Counter, defaultdict


T = int(input())

for _ in range(T):
    n = int(input())
    team_num = list(map(int, input().split()))

    team_cnt = Counter(team_num)
    score_dict = defaultdict(list)
    no = 1
    for i in range(n):
        if team_cnt.get(team_num[i]) == 6:
            score_dict[team_num[i]].append(no)
            no += 1

    winner = 0
    min_score = int(1e9)

    for team_no in score_dict.keys():
        score = sum(score_dict[team_no][:4])
        if score == min_score:
            if score_dict[team_no][4] < score_dict[winner][4]:
                winner = team_no
        elif score < min_score:
            winner = team_no
            min_score = score

    print(winner)
