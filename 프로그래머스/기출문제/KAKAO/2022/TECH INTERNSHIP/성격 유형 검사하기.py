def solution(survey, choices):
    answer = ''

    type_dict = dict()
    for s in 'TRCFJMAN':
        type_dict[s] = 0

    type_collection = [
        ('T', 'R'),
        ('C', 'F'),
        ('J', 'M'),
        ('A', 'N')
    ]
    score_dict = {
        1: 3, 2: 2, 3: 1,
        4: 0, 5: 1, 6: 2, 7: 3
    }

    for i in range(len(choices)):
        if choices[i] <= 3:
            type_dict[survey[i][0]] += score_dict[choices[i]]
        elif choices[i] >= 5:
            type_dict[survey[i][1]] += score_dict[choices[i]]

    for tp in type_collection:
        if type_dict[tp[0]] > type_dict[tp[1]]:
            answer += tp[0]
        elif type_dict[tp[0]] < type_dict[tp[1]]:
            answer += tp[1]
        else:
            if tp[0] < tp[1]:
                answer += tp[0]
            else:
                answer += tp[1]

    return answer
