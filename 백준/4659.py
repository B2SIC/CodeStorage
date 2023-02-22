import sys
import string

input = sys.stdin.readline

while True:
    get_pw = input().rstrip()
    if get_pw == "end":
        break

    is_acceptable = True

    # 모음 하나를 반드시 포함해야한다.
    for alpha in ['a', 'e', 'i', 'o', 'u']:
        if alpha in get_pw:
            break
    else:
        is_acceptable = False

    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
    # 자음, 모음을 각각 같은 알파벳으로 치환하여 검사
    transf_pw = ''
    for alpha in get_pw:
        if alpha in 'aeiou':
            transf_pw += 'a'
        else:
            transf_pw += 'b'
    # 검사
    for alpha in 'ab':
        alpha = alpha * 3

        if alpha in transf_pw:
            is_acceptable = False
            break

    # 같은 글자가 연속으로 두번 오면 안되나, ee와 oo는 허용
    for alpha in string.ascii_lowercase.replace('e', '').replace('o', ''):
        alpha = alpha * 2
        if alpha in get_pw:
            is_acceptable = False
            break

    if is_acceptable:
        print(f"<{get_pw}> is acceptable.")
    else:
        print(f"<{get_pw}> is not acceptable.")
