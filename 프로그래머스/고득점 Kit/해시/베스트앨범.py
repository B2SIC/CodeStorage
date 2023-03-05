from collections import defaultdict


def solution(genres, plays):
    answer = []
    musics = defaultdict(list)
    genre_with_played = defaultdict(int)

    for i in range(len(genres)):
        musics[genres[i]].append((i, plays[i]))
        genre_with_played[genres[i]] += plays[i]

    for key in musics.keys():
        musics[key].sort(key=lambda x: (x[1], -x[0]))

    for key, _ in sorted(genre_with_played.items(), key=lambda x: x[1], reverse=True):
        for i in range(2):
            if musics[key]:
                answer.append(musics[key].pop()[0])

    return answer
