
v,l=map(int,input().split())
m=0
for i in range(0,v):
    d=list(map(int,input().split()))
    if sum(d)>m:
        m=sum(d)
print(m)