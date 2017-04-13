#include <cstdio>
#include <algorithm>
#include <vector>

typedef std::pair<long long, long long> pii;
long long n, perm[12], bad, ans;
std::vector<pii> points;

long long cross(pii a, pii o, pii b) {
    return (a.first - o.first) * (b.second - o.second) -
           (b.first - o.first) * (a.second - o.second);
}

long long intersects(pii a, pii b, pii c, pii d) {
    if (a == c || a == d || b == c || b == d) return false;
    return cross(a, b, c) * cross(a, b, d) <= 0 &&
           cross(d, c, a) * cross(d, c, b) <= 0;
}

int main() {
    scanf("%d", &n);
    for (int i = 0, a, b; i < n; i++) {
        scanf("%d %d", &a, &b);
        points.push_back(std::make_pair(a, b));
        perm[i] = i;
    }
    do {
        perm[n] = 0;
        bad = 0;
        for (int i = 0; i < n && !bad; i++) {
            for (int j = 0; j < n && !bad; j++) {
                if (intersects(points[perm[i]], points[perm[i + 1]],
                               points[perm[j]], points[perm[j + 1]])) {
                    bad = 1;
                }
            }
        }
        if (!bad) ans++;
    } while (std::next_permutation(perm, perm + n) && !perm[0]);
    printf("%lld\n", ans / 2);
}