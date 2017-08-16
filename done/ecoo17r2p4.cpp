#include <bits/stdc++.h>
#define MOD 1000000007

int n;
long long last[10005], cur[10005];

void do_case(){
    scanf("%d",&n);
    memset(last, 0, sizeof(last));
    memset(cur, 0, sizeof(cur));
    n--;
    last[0]=cur[0]=1;
    for (int i=1; i<=n; i++) {
        for (int j=0; j<=i; j++) cur[i-j]=last[j];
        for (int j=1; j<=i; j++) cur[j]=(cur[j]+cur[j-1])%MOD;
        for (int i = 0; i < 10005; i++) last[i] = cur[i];
    }
    int ans=0;
    for (int i=0; i<=n; i++) ans=(ans+cur[i])%MOD;
    printf("%d\n",ans);
}

int T = 10;

int main(){
    while (T--) do_case();
}