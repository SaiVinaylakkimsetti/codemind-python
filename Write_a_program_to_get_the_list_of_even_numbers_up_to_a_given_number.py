n,b = map(int,input().split())
if n%2==0:
    for i in range(n,b+1,2):
        
        print(i,end=' ')
else:
    for x in range(n+1,b+1,2):
        print(x,end=' ')
    