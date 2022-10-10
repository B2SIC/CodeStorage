# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int, input().split())

data_list = []
for _ in range(n):
	name, height = input().split()
	data_list.append((name, float(height)))

data_list.sort(key=lambda x:(x[0], x[1]))
name, height = data_list[k - 1]
print(f"{name} {height:.2f}")
