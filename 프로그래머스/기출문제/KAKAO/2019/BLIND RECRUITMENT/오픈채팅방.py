from collections import defaultdict


def solution(record):
    answer = []

    user_db = defaultdict(str)
    for rc in record:
        commands = rc.split()
        if commands[0] in ["Enter", "Change"]:
            user_db[commands[1]] = commands[2]

    for rc in record:
        commands = rc.split()

        if commands[0] == "Enter":
            answer.append(f"{user_db[commands[1]]}님이 들어왔습니다.")
        elif commands[0] == "Leave":
            answer.append(f"{user_db[commands[1]]}님이 나갔습니다.")

    return answer
