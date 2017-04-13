#include <cstdio>
#include <cmath>

#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define abs(a) ((((a) > 0)) ? (a) : (-(a)))

long long fx, fy, fr, wx, wy, wr, ans = 0;
int main() {
    scanf("%lld %lld %lld %lld %lld %lld", &fx, &fy, &fr, &wx, &wy, &wr);
    for (int y = fy - fr; y <= fy + fr; y++) {
        long long da = sqrt(fr * fr - (y - fy) * (y - fy));
        long long a = fx - da, b = fx + da;
        long long db = wr - abs(y - wy);
        long long c = wx - db, d = wx + db;
        long long res = max(0, min(b, d) - max(c, a) + 1);
        if (y == fy && fx != wx && c <= fx && fx <= d) ans--;
        if (y == wy && a <= wx && wx <= b) ans--;
        ans += res;
    }
    printf("%lld\n", ans);
}