def check_palindrome(s):
    return s == s[::-1]

n = int(input())

for i in range(1, n + 1):
    word = input()
    if check_palindrome(word.lower()):
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")
