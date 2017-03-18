#include <cstdio>
#include <vector>
#include <bitset>

#define getchar() (*_pinp?*_pinp++:(_inp[fread(_pinp=_inp, 1, 4096, stdin)]='\0', *_pinp++))
char _inp[4097], *_pinp=_inp;
#define scan(x) do{while((x=getchar())<'-'); _ssign=x=='-'; if(_ssign) while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0'); x=_ssign?-x:x;}while(0)
char _; bool _ssign;

int n, m, k, a, b, sz[1000005], root[1000005], cycle[1000005];
std::bitset<1000005> vis;
int adj[1000005];
int ans, cuts, last_checked;

int find(int n) {
    if (root[n] != n) root[n] = find(root[n]);
    return root[n];
}

int main() {
    scan(n); scan(m); scan(k);
    if (k == 1) {
        printf("%d %d\n", n, m);
        return 0;
    }
    for (int i = 0; i <= n; i++) root[i] = i, sz[i] = 1;
    for (int i = 0; i < m; i++) {
        scan(a); scan(b);
        const int ar = find(a), br = find(b);
        if (ar != br) {
            root[ar] = br;
            sz[br] += sz[ar];
        } else {
            cycle[ar] = 1;
        }
        adj[a]++, adj[b]++;
    }
    for (int i = 1; i <= n; i++) {
        const int rt = find(i);
        if (vis[rt]) continue;
        vis[rt] = 1;
        const int size = sz[rt];
        if (size < k) continue;
        ans += size / k;
        if (!cycle[rt]) {
            if (size % k == 0) {
                cuts += size / k - 1;
            } else {
                cuts += size / k;
            }
        } else {
            if (size % k == 0 && size != k) {
                cuts += size / k;
            } else if (size != k) {
                cuts += size / k + 1;
            }
        }
    }
    printf("%d %d\n", ans * k, cuts);
}