#include <bits/stdc++.h>

int n;
char m[1024][1024];
int ans;
int keys;

void reset() {
    ans=0;
    keys=0;
}

int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};

void dfs(int i, int j) {
    for (int k=0; k<4; k++) {
        int i2=i+dx[k];
        int j2=j+dy[k];
        if (i2<0) continue;
        if (i2>=n) continue;
        if (j2<0) continue;
        if (j2>=n) continue;
        char ch=m[i2][j2];
        if (ch=='S') continue;
        if (ch=='#') continue;
        if (ch=='K') {
            m[i2][j2]='S';
            keys++;
            dfs(i2,j2);
        }
        else if (ch=='.') {
            m[i2][j2]='S';
            dfs(i2,j2);
        }
        else if (ch=='T') {
            ans++;
            m[i2][j2]='S';
            dfs(i2,j2);
        }
        else if (keys>=ch-'0') {
            m[i2][j2]='S';
            dfs(i2,j2);
        }
    }
}

void do_case() {
    scanf("%d",&n);
    for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                scanf(" %c",&m[i][j]);
            }
    }
    for (int asdf=0; asdf<10; asdf++) {
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (m[i][j]=='S') dfs(i,j);
            }
        }
    }
    printf("%d\n",ans);
}

int T = 10;

int main() {
    while (T--) reset(), do_case();
}