n = int(input())
adv = list(map(int, input().split()))

adv.sort()
group = 0
member = 0
for i in adv:
    member += 1
    if member >= i:
        group += 1
        member = 0

print(group)
