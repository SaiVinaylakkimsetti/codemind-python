r,c = map(int,input().split())
s=0
m=0
for i in range(0,r):
    inner_list = list(map(int,input().split()))
    if i%2==0:
        s+=sum(inner_list)
    else:
        m+=sum(inner_list)
print(s,m)