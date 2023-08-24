l = int(input())
a = l//2
while a*a>l :
    a=(a+l//a)//2
if a*a==l:
    print('True')
else:
    print('False')