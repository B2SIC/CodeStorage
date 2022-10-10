def solution(arr):
    answer = 1
    arr.sort()

    max_in_arr = max(arr)
    i = 2
    while i <= max_in_arr:
        divide_idx_list = []
        for j in range(len(arr)):
            if arr[j] % i == 0:
                divide_idx_list.append(j)

        if len(divide_idx_list) >= 2:
            for idx in divide_idx_list:
                arr[idx] = arr[idx] // i
            answer *= i
            i = 2
        else:
            i += 1

    for num in arr:
        answer *= num

    return answer
