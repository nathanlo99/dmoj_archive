import sys
input = sys.stdin.readline

floor=int

for _ in range(10):
    x=int(input())
    a,b,c,d=map(float,input().split())
    n=int(input())
    total=floor(n*a+1e-15)*12 + floor(n*b+1e-15)*10 + floor(n*c+1e-15)*7 + floor(n*d+1e-15)*5
    #print(total,x)
    if total>=x*2: print("NO")
    else: print("YES")