from math import ceil


def time_calculator(in_time, out_time):
    out_time = int(out_time.split(':')[0]) * 60 + int(out_time.split(':')[1])
    in_time = int(in_time.split(':')[0]) * 60 + int(in_time.split(':')[1])
    return out_time - in_time


def fee_calculator(fees, total_time):
    standard_time, standard_fee, unit_time, unit_fee = fees

    if total_time <= standard_time:
        return standard_fee
    else:
        return standard_fee + (ceil((total_time - standard_time) / unit_time) * unit_fee)


def record_reader(fees, records, parking_time, parking_hist):
    for record in records:
        time, car_num, status = record.split()

        if status == "IN":
            parking_hist[car_num] = time
        elif status == "OUT":
            total_time = time_calculator(parking_hist[car_num], time)
            parking_hist[car_num] = '-'

            if parking_time.get(car_num, -1) == -1:
                parking_time[car_num] = total_time
            else:
                parking_time[car_num] += total_time
    return parking_time, parking_hist


def solution(fees, records):
    answer = []
    parking_time = dict()
    parking_hist = dict()

    parking_time, parking_hist = record_reader(fees, records, parking_time, parking_hist)

    for car_num, time in parking_hist.items():
        if time != '-':
            make_record = [f"23:59 {car_num} OUT"]
            parking_time, parking_hist = record_reader(fees, make_record, parking_time, parking_hist)

    for car_num, time in sorted(parking_time.items()):
        answer.append(fee_calculator(fees, time))

    return answer
