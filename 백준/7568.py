num = int(input())
size_list = list()

for i in range(num):
    weight, height = map(int, input().split())
    size_list.append([weight, height, 1])

for i in range(len(size_list)):
    weight, height, _ = size_list[i]

    for j in range(len(size_list)):
        weight2, height2, _ = size_list[j]

        if weight < weight2 and height < height2:
            size_list[i][2] += 1

    print(size_list[i][2], end=' ')
