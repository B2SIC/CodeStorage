def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        answer.append(bin(a | b).split('0b')[1].zfill(n).replace('1', '#').replace('0', ' '))  # zfill 함수
        # answer.append(bin(a | b).split('0b')[1].rjust(n, '0').replace('1', '#').replace('0', ' '))  # rjust 함수
    return answer
