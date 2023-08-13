def is_palindrome(w):
    return  w == w[::-1]
w=input()
if is_palindrome(w):
    print("True")
else:
    print("False")