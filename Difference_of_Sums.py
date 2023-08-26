n = int(input())
s = 0
c = 0
for i in range(1,n+1):
    s = s+(i*i)
for j in range(1,n+1):
    c = c+j
    x = c**2
print(abs(s-x))

     