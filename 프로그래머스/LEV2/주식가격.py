from collections import deque


def bigger_than_count(price, l):
    cnt = 0
    for elem in l:
        cnt += 1

        if price > elem:
            break
    return cnt


def solution(prices):
    answer = []
    prices = deque([i for i in prices])

    while prices:
        val = prices.popleft()
        answer.append(bigger_than_count(val, prices))

    return answer
