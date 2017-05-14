import sys
input = sys.stdin.readline

def do_case():
    n=int(input())
    people=[]
    for _ in range(n):
        t=list(map(int,input().strip().split('.')))
        t[0]=1
        people.append(t)
    people.sort()
    st=[1]
    ans=1
    for i in range(n):
        #print(people[i])
        # find diff between people i,i+1
        for j in range(len(people[i])):
            if j<len(st):
                if st[j]==people[i][j]: continue
                else:
                    ans+=people[i][j]-st[j]
                    while len(st)>j: st.pop(-1)
                    #print("pop to",st)
                    st.append(people[i][j])
            elif j>=len(st):
                ans+=people[i][j]
                st.append(people[i][j])
    print(ans % 1000000007)

T = 10
for _ in range(T):
    do_case()