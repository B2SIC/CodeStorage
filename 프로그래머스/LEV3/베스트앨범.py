from collections import defaultdict


def solution(genres, plays):
    answer = []

    # Nested Dictionary 생성
    # ex) {'classic': {0: 500, 2: 150, 3: 800}, 'pop': {1: 600, 4: 2500}}
    hist = defaultdict(dict)
    for i, data in enumerate(zip(genres, plays)):
        genre, play = data
        hist[genre][i] = play

    sorted_hist = sorted(hist.items(), key=lambda x: sum(x[1].values()), reverse=True)
    for genre, data in sorted_hist:
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)[:2]
        for k in range(min(2, len(sorted_data))):
            answer.append(sorted_data[k][0])

    return answer
