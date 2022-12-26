import heapq


def solution(operations):
    heap = []
    reverse_key = lambda x: x * (-1)
    for op in operations:
        command, value = op.split()
        value = int(value)

        if command == 'I':
            heapq.heappush(heap, value)
        elif command == 'D' and heap:
            if value == 1:
                # Max Heap 으로 전환
                heap = list(map(reverse_key, heap))
                heapq.heapify(heap)
                heapq.heappop(heap)

                # 다시 Min Heap 으로 전환
                heap = list(map(reverse_key, heap))
                heapq.heapify(heap)
            elif value == -1:
                heapq.heappop(heap)

    if not heap:
        answer = [0, 0]
    else:
        answer = [max(heap), min(heap)]
    return answer
