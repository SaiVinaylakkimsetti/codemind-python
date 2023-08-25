n = int(input())
r=0
s=n
while(n>0):
    rem=n%10
    r=(r*10)+rem
    n=n//10
if s==r:
    print("Palindrome")
else:
    print("Not Palindrome")
    