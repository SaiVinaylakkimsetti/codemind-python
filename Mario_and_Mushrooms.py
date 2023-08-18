n=int(input())
b=n%3
if b==0:
    print('NORMAL')
elif b==2:
    print('SMALL')
else:
    print('HUGE')