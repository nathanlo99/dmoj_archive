import sys
input = sys.stdin.readline

def do_case():
    n,m=map(int,input().split())
    d={}
    for _ in range(4):
        a,b=input().split()
        d[a]=b
    floors=input().strip()
    for _ in range(m-1):
        floor2=""
        for i in range(n):
            floor2+=d[floors[i-1]+floors[(i+1)%n]]
        #print(floors,floor2)
        floors=floor2
    print(floors)
    input()

t = 10
for _ in range(t):
    do_case()