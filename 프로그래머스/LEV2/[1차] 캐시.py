def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.append(cache.pop(cache.index(city)))
        else:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
            answer += 5
    return answer
