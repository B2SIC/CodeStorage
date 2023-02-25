def solution(word):
    mo_um = ['A', 'E', 'I', 'O', 'U']
    mo_um_2 = []
    mo_um_3 = []
    mo_um_4 = []
    mo_um_5 = []

    for s in mo_um:
        for ss in mo_um:
            mo_um_2.append(s + ss)

    for s in mo_um:
        for ss in mo_um_2:
            mo_um_3.append(s + ss)

    for s in mo_um:
        for ss in mo_um_3:
            mo_um_4.append(s + ss)

    for s in mo_um:
        for ss in mo_um_4:
            mo_um_5.append(s + ss)

    word_dict = mo_um + mo_um_2 + mo_um_3 + mo_um_4 + mo_um_5
    word_dict.sort()

    return word_dict.index(word) + 1
