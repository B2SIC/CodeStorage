from collections import defaultdict


def score_diff(apeach_score, lion_score):
    score = 0
    for i in range(0, 11):
        if lion_score[i] > apeach_score[i]:
            score += 10 - i
        else:
            if apeach_score[i] == 0:
                continue
            score -= 10 - i
    return score


def solution(n, info):
    lion_scores = []

    # 전범위 탐색 후 가능한 조합 찾기
    for i in range(0, 2048):
        lion_score = []
        bit = bin(i).split('0b')[1].zfill(11)

        for j in range(len(bit)):
            if bit[j] == '0':
                lion_score.append(0)
            else:
                lion_score.append(info[j] + 1)

        if sum(lion_score) <= n:
            lion_scores.append(lion_score)

    max_score_diff = -1
    max_lion_scores = defaultdict(list)

    for lion_score in lion_scores:
        get_score = score_diff(info, lion_score)
        if max_score_diff <= get_score:
            max_score_diff = get_score
            max_lion_scores[get_score].append(lion_score)

    if max_lion_scores and max_score_diff > 0:
        max_lion_scores = sorted(max_lion_scores.items(), reverse=True)[0][1]

        for i in range(len(max_lion_scores)):
            diff = n - sum(max_lion_scores[i])
            if diff > 0:
                for j in range(10, -1, -1):
                    while diff > 0 and max_lion_scores[i][j] + 1 < info[j]:
                        max_lion_scores[i][j] += 1
                        diff -= 1

        max_idx = 0
        max_idx_count = 0
        answer = []

        for i in range(len(max_lion_scores)):
            for j in range(10, -1, -1):
                if max_lion_scores[i][j] != 0:
                    if j > max_idx:
                        max_idx = j
                        max_idx_count = max_lion_scores[i][j]
                        answer = max_lion_scores[i]
                    elif j == max_idx and max_lion_scores[i][j] > max_idx_count:
                        max_idx_count = max_lion_scores[i][j]
                        answer = max_lion_scores[i]
    else:
        answer = [-1]
    return answer
