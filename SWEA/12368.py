T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    time = (a + b) % 24
    print(f"#{i + 1} {time}")
