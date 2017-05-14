import sys
input = sys.stdin.readline

def do_case():
    f,d=map(int,input().split())
    g=[]
    tot=[0]*f
    for _ in range(d):
        t=list(map(int,input().split()))
        for i in range(f):
            tot[i]+=t[i]
        g.append(sum(t))
    ans=0
    for i in g+tot:
        if i%13==0:
            ans+=i//13
    print(ans)

T = 10
for _ in range(T):
    do_case()