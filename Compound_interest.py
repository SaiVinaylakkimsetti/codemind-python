p,r,t=map(int,input().split())
p = p*((1+r/100.00)**t)

print(f"{p:.2f}")