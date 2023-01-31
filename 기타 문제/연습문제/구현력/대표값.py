# import sys
#
# sys.stdin = open('in1.txt', 'rt')

n = int(input())
scores = list(map(int, input().split()))

# round 함수는 round_half_even 방식 (round_half_up 방식이 필요함)
# round_half_even -> 특정 숫자 값에 가장 가까운 지정된 정밀도의 숫자 값을 리턴한다.
avg = int((sum(scores) / n) + 0.5)
diff_scores = []
for score in scores:
    diff_scores.append(abs(avg - score))

min_diff = float('inf')
min_score = 0
min_idx = -1

for i in range(len(diff_scores)):
    if diff_scores[i] < min_diff or (diff_scores[i] == min_diff and min_score < scores[i]):
        min_diff = diff_scores[i]
        min_score = scores[i]
        min_idx = i + 1

print(avg, min_idx)
