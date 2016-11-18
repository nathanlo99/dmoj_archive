#include <bits/stdc++.h>
using namespace std;
const int MOD=1000000007;
struct NODE{ int l, r, h; bool lazy;} seg[3000002];
struct BOOK{ int l, r, w;} book[500003];
int N, tot; set<int> s; unordered_map<int, int>mp; vector<int> pos; long long ans;
void push_down(int rt){
    seg[2*rt].h = max(seg[rt].h, seg[2*rt].h);
    seg[2*rt+1].h = max(seg[rt].h, seg[2*rt+1].h);
    seg[2*rt].lazy = seg[2*rt+1].lazy = true; seg[rt].lazy = false;
}
void build_tree(int l, int r, int rt){
    seg[rt].l=l; seg[rt].r=r;
    if(l==r) return;
    int mid = (l+r)/2;
    build_tree(l, mid, 2*rt); build_tree(mid+1, r, 2*rt+1);
}
int query(int l, int r, int rt){
    if(seg[rt].l==l && seg[rt].r==r) return seg[rt].h;
    if(seg[rt].lazy) push_down(rt);
    int mid = (seg[rt].l + seg[rt].r)/2;
    if(r<=mid) return query(l, r, 2*rt);
    else if(l > mid) return query(l, r, 2*rt+1);
    else return max(query(l, mid, 2*rt), query(mid+1, r, 2*rt+1));
}
void update(int l, int r, int val, int rt){
    if(seg[rt].l==l && seg[rt].r==r){
        seg[rt].h = val; seg[rt].lazy=true;
        return;
    }
    if(seg[rt].lazy) push_down(rt);
    int mid = (seg[rt].l+seg[rt].r)/2;
    if(r<=mid) update(l, r, val, 2*rt);
    else if(l > mid) update(l, r, val, 2*rt+1);
    else{
        update(l, mid, val, 2*rt); update(mid+1, r, val, 2*rt+1);
    }
    seg[rt].h = max(seg[2*rt].h, seg[2*rt+1].h);
}
int main(){
    //freopen("test.txt", "r", stdin);
    scanf("%d", &N);
    for(int i=1; i<=N; i++){
        scanf("%d %d %d", &book[i].l, &book[i].r, &book[i].w);
        ans -= 1LL*book[i].r*book[i].w; book[i].r+=book[i].l;
        s.insert(book[i].l); s.insert(book[i].r);
    }
    for(int x: s){
        mp[x] = tot++; pos.push_back(x);
    }
    build_tree(1, tot, 1);
    for(int i=1; i<=N; i++){
        int lp=mp[book[i].l]+1, rp=mp[book[i].r];
        int rmq = query(lp, rp, 1);
        update(lp, rp, rmq+book[i].w, 1);
    }
    for(int i=1; i<tot; i++){
        int h = query(i, i, 1);
        ans += 1LL*h*(pos[i]-pos[i-1]);
    }
    printf("%lld\n", ans%MOD);
}