p=int(input())
r=int(input())
t=int(input())
ci=((r/100)+1)**t
d=(p*ci)-p
print(f"{d:.2f}")