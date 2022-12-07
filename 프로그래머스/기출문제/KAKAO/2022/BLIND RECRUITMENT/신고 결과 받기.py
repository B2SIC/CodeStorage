def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = {id: [] for id in id_list}

    for content in set(report):
        report_from, report_to = content.split()
        report_dict[report_to].append(report_from)

    for key, value in report_dict.items():
        if len(value) >= k:
            for id in value:
                answer[id_list.index(id)] += 1

    return answer
