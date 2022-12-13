from itertools import permutations


def solution(k, dungeons):
    answer = -1
    permut_idx = [i for i in range(len(dungeons))]

    for seq in permutations(permut_idx, len(dungeons)):
        get_k = k
        total_cost = 0

        for i in seq:
            require, cost = dungeons[i]

            if require > get_k:
                break

            get_k -= cost
            total_cost += 1

        if answer < total_cost:
            answer = total_cost

    return answer
