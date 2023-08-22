b = int(input())
if b<=10000:
    da=.8*b
    hra=.2*b
elif b<=20000:
    da=.9*b
    hra=.25*b
elif b>20000:
    da=.95*b
    hra=.3*b
s = b+da+hra
print(f"{s:.2f}")