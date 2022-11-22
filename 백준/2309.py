heights = []
for _ in range(9):
  heights.append(int(input()))

sum = sum(heights)
idx, idx2 = 0, 0
for i in range(8):
  for j in range(i + 1, 9):
    if sum - (heights[i] + heights[j]) == 100:
      idx, idx2 = i, j
      break

del heights[idx2]
del heights[idx]
print(*sorted(heights), sep='\n')
