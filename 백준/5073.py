# 뭔가 아쉬운 코드.. 개선할 수 있을 것 같다.
while True:
    nums = list(map(int, input().split()))
    if nums == [0, 0, 0]:
        break
    nums.sort()
    a, b, c = nums

    if a == b and b == c:
        print("Equilateral")
    else:
        if c < a + b:
            if a == b or b == c:
                print("Isosceles")
            else:
                print("Scalene")
        else:
            print("Invalid")
