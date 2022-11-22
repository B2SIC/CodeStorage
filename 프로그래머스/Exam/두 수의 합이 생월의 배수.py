import random
import time


def random_generator(num):
    nums = list(random.sample(range(1, num + 1), num))
    return nums


def brute_force_method(nums, m):
    start = time.time()
    result = 0
    length = len(nums)

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if (nums[i] + nums[j]) % m == 0:
                result += 1
    end = time.time()
    return [result, end - start]


def modulo_add_method(nums, m):
    start = time.time()
    result = 0
    modulo_map = dict()

    for num in nums:
        modulo = num % m
        if modulo_map.get(modulo, -1) == -1:
            modulo_map[modulo] = [num]
        else:
            modulo_map[modulo].append(num)

    set_range = (m // 2) + 1
    for i in range(0, set_range):
        if i == 0:
            if modulo_map.get(i, -1) != -1:
                if len(modulo_map[i]) >= 2:
                    length = len(modulo_map[i])
                    result += (length * (length - 1)) // 2
        else:
            partner = m - i

            if partner == i:
                if modulo_map.get(i, -1) != -1:
                    if len(modulo_map[i]) >= 2:
                        length = len(modulo_map[i])
                        result += (length * (length - 1)) // 2
            else:
                if modulo_map.get(i, -1) != -1 and modulo_map.get(partner, -1) != -1:
                    result += len(modulo_map[i]) * len(modulo_map[partner])

    end = time.time()
    return [result, end - start]


number_list = random_generator(200000)  # 최대 200,000
print("MOD 연산")
modulo_method_result = modulo_add_method(number_list, 12)
print(modulo_method_result)
print("모든 비교 연산")
brute_method_result = brute_force_method(number_list, 12)
print(brute_method_result)
