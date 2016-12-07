#include <set>
#include <map>
#include <cstdio>

typedef struct {
    int x1, y1, x2, y2, t1;
} pane;

int n, k, t, x1, y1, x2, y2, t1, xn = 1, yn = 1;
int da[2001][2001], valuex[2001], valuey[2001];
std::map<int, int> lookupx, lookupy;
pane panes[1001];
std::set<int> x;
std::set<int> y;

int main() {
    scanf("%d %d", &n, &t);
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d %d %d", &x1, &y1, &x2, &y2, &t1);
        panes[i] = (pane){x1, y1, x2, y2, t1};
        x.insert(x1); x.insert(x2); y.insert(y1); y.insert(y2);
    }

    for (int v : x) {
        valuex[xn - 1] = v, lookupx[v] = xn, xn++;
    }

    for (int v : y) {
        valuey[yn - 1] = v, lookupy[v] = yn, yn++;
    }

    for (int i = 0; i < n; i++) {
        x1 = lookupx[panes[i].x1], y1 = lookupy[panes[i].y1];
        x2 = lookupx[panes[i].x2], y2 = lookupy[panes[i].y2];
        t1 = panes[i].t1;
        da[x1][y1] += t1, da[x1][y2] -= t1;
        da[x2][y1] -= t1, da[x2][y2] += t1;
    }
    
    long long ans = 0LL;
    for (int i = 1; i < x.size(); i++) {
        for (int j = 1; j < y.size(); j++) {
            da[i][j] += da[i - 1][j] + da[i][j - 1] - da[i - 1][j - 1];
            if (da[i][j] >= t) {
                ans += 1LL * (valuex[i] - valuex[i - 1]) * (valuey[j] - valuey[j - 1]);
            }
        }
    }
    
   
    printf("%lld\n", ans);
}