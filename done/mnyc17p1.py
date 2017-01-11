input()
stuff=sum(map(int,input().split()))
i=1<<30
while not stuff&i: i>>=1
print(i)