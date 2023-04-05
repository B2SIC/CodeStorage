from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_done = []
    truck_weights = deque(truck_weights)
    truck_crossing = deque()

    time = 0
    status_weight = 0
    while truck_crossing or truck_weights:
        for i in range(len(truck_crossing)):
            truck_crossing[i][1] += 1

        if truck_crossing and (truck_crossing[0][1] >= bridge_length):
            popped_data = truck_crossing.popleft()
            truck_done.append(popped_data[0])
            status_weight -= popped_data[0]

        if len(truck_crossing) < bridge_length:
            if truck_weights and (status_weight + truck_weights[0] <= weight):
                nx = truck_weights.popleft()
                status_weight += nx
                truck_crossing.append([nx, 0])

        time += 1
    return time
