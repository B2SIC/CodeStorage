def sum_of_truck(in_prog: list):
    res = 0
    for weight, time in in_prog:
        res += weight
    return res


def solution(bridge_length, weight, truck_weights):
    done = []  # 다리를 지난 트럭
    in_prog = []  # 다리를 건너는 중인 트럭
    time = 0  # 경과 시간
    while True:
        if not truck_weights and not in_prog:
            break

        # 다리를 지나는 트럭 처리
        for elem in in_prog:
            elem[1] -= 1
        # 다 지난 트럭 제거
        for elem in in_prog:
            if elem[1] == 0:
                done.append(in_prog.pop(0)[0])

        # 다리에 올라올 수 있는 트럭 처리
        if truck_weights:
            if (sum_of_truck(in_prog) + truck_weights[0] <= weight) and (len(in_prog) + 1 <= bridge_length):
                in_prog.append([truck_weights.pop(0), bridge_length])
        time += 1

    return time
