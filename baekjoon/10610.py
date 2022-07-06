# https://ko.wikipedia.org/wiki/배수_판정법

n = input()

n_list = list(map(int, n))

if sum(n_list) % 3 != 0:
  print(-1)
else:
  n_list.sort(reverse=True)

  if n_list[-1] != 0:
    print(-1)
  else:
    print(''.join(map(str, n_list)))
