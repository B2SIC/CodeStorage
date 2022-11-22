n = int(input())

result = 0
end_time = 0
room_list = list()

for i in range(n):
  s, e = map(int, input().split())
  room_list.append((s, e))

room_list.sort(key=lambda x:(x[1], x[0]))

for room in room_list:
  s, e = room
  if end_time <= s:
    result += 1
    end_time = e

print(result)
