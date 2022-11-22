n = int(input())

ropes = list()
w_list = list()
for i in range(n):
  get_rope = int(input())
  ropes.append(get_rope)

ropes.sort()
k = len(ropes)
for rope in ropes:
  w_list.append(k * rope)
  k -= 1

print(max(w_list))
