l = int(input())
vi = 0
for i in range(1,l):
    if l%i==0:
        vi+=i
if vi==l:
    print('True')
else:
    print('False')