from collections import Counter


def solution(participant, completion):
    # Counter 객체는 사칙연산과 집합연산이 가능하다.
    res = Counter(participant) - Counter(completion)
    return list(res.keys())[0]
