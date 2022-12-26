def solution(msg):
    answer = []

    idx_dict = {alpha: i + 1 for i, alpha in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    i = 0
    j = i + 1
    count = len(idx_dict) + 1
    while i < len(msg):
        base = msg[i]

        j = i + 1
        if j >= len(msg):
            answer.append(idx_dict[base])
            break

        check_msg = base
        while True:
            check_msg += msg[j]

            if check_msg not in idx_dict:
                answer.append(idx_dict[base])
                idx_dict[check_msg] = count
                count += 1
                break

            base = check_msg
            i += 1
            j += 1

            if j >= len(msg):
                answer.append(idx_dict[base])
                break
        i += 1
    return answer
