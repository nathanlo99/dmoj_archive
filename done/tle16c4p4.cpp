#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
int N, M, Q, st, ed, cost[100002], par[100002], cnt; long long len, ans; vector<pii> adj[100002]; bool vis[100002];
void dfs1(int u, int par, long long dis){
    vis[u] = true;
    if(dis > len) { st=u; len=dis; }
    for(auto p: adj[u]){
        int v = p.first, d = p.second;
        if(!vis[v]) dfs1(v, u, dis+d);
    }
}
void dfs2(int u, int fa, long long dis){
    if(dis > len) { len=dis; ed=u; }
    for(auto p: adj[u]){
        int v = p.first, d = p.second;
        if(v == fa) continue;
        par[v]=u; cost[v]=d; dfs2(v, u, dis+d);
    }
}
int main(){
    //freopen("test.txt", "r", stdin);
    scanf("%d %d %d", &N, &M, &Q);
    for(int i=0, x, y, z; i<M; i++){
        scanf("%d %d %d", &x, &y, &z);
        adj[x].push_back(make_pair(y, z)); adj[y].push_back(make_pair(x, z));
    }
    for(int i=1; i<=N; i++){
        if(!vis[i]){
            len = -1; dfs1(i, -1, 0);
            len = -1; dfs2(st, -1, 0);
            if(Q==1) ans += len + 1;
            else{
                long long R = 1e18, d = 0;
                for(int u=ed; u!=0; u=par[u]){
                    d += cost[u]; R=min(R, max(d, len-d));
                }
                if( R > ans) { ans=R; cnt=1; }
                else if( R==ans ) cnt++;
            }
        }
    }
    if(Q==1) printf("%lld\n", ans-1);
    else printf("%lld\n", cnt==1? ans: ans+1);
}