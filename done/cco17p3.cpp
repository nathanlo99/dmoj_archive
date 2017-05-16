#include <cstdio>
#include <tuple>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>

#define mod 1000000007

using namespace std;

static pair<long long, long long> get_index(long long n) {
    long long pre = 1, h = 60;
    while (n != 1) {
        if (n % 2 == 1) pre += 2 * ((1LL << h) - 1);
        pre++; n /= 2; h--;
    }
    return make_pair(pre, pre + 4 * ((1LL << h) - 1) + 1);
}

long long n, q, x, y, c, x1, yy1, x2, y2, type;
long long ans[200005];

int cx, cy;
vector<tuple<long long, int, long long, long long, long long> > events;
set<long long> xs, ys;
map<long long, int> lookupx, lookupy;
long long bit[1000000];

void update(int idx, long long amt) {
    for (int a = idx; a <= 1000000; a += a & -a) bit[a] = (bit[a] + amt) % mod;
}

void update(int l, int r, long long c) {
    update(l, c);
    update(r + 1, -c);
}

long long query(int idx) {
    long long res = 0;
    for (int a = idx; a > 0; a -= a & -a) res += bit[a];
    return res;
}

int main() {
    scanf("%lld %lld", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld", &x, &y, &c);
        tie(x1, x2) = get_index(x); tie(yy1, y2) = get_index(y);
        events.push_back(make_tuple(x1, 1, yy1, y2, c));
        events.push_back(make_tuple(x2, 3, yy1, y2, -c));
        xs.insert(x1); xs.insert(x2); ys.insert(yy1); ys.insert(y2);
    }

    for (int i = 0; i < q; i++) {
        scanf("%lld %lld", &x, &y);
        tie(x1, x2) = get_index(x); tie(yy1, y2) = get_index(y);
        events.push_back(make_tuple(x1, 2, yy1, 0, i));
        xs.insert(x1); ys.insert(yy1);
    }
    
    for (long long xx : xs) lookupx[xx] = ++cx;
    for (long long yy : ys) lookupy[yy] = ++cy;

    sort(events.begin(), events.end());

    for (auto v : events) {
        tie(x, type, yy1, y2, c) = v;
        if (type == 2) {
            ans[c] = query(lookupy[yy1]);
        } else {
            update(lookupy[yy1], lookupy[y2], c);
        }
    }

    for (int i = 0; i < q; i++) printf("%lld\n", ans[i]);
}