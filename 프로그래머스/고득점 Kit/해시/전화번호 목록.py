def solution(phone_book):
    phone_map = {phone: 1 for phone in phone_book}

    for phone_number in phone_book:
        make_phone = ''
        for s in phone_number:
            make_phone += s

            if phone_number != make_phone and phone_map.get(make_phone) is not None:
                return False
    return True
