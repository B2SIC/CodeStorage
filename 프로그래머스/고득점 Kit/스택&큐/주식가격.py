'''
3 / 0 , [3]
2 / 1 0, [2, 3] min = 2
3 / 1 1 0 [3, 2, 3] min = 2
2 / 3 1 1 0 [2, 3, 2, 3] min = 2
1 / 4 3 1 1 0 [1, 2, 3, 2, 3] min = 1
'''
from collections import deque


def solution(prices):
    answer = deque()
    min_value = 0
    popped_prices = deque()
    while prices:
        val = prices.pop()

        if not popped_prices:
            popped_prices.append(val)
            answer.appendleft(0)
            min_value = val
        else:
            if val <= min_value:
                min_value = val
                answer.appendleft(len(popped_prices))
            else:
                for i in range(len(popped_prices)):
                    if popped_prices[i] < val:
                        answer.appendleft(i + 1)
                        break

            popped_prices.appendleft(val)

    return list(answer)
