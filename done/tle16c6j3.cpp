#include <cstdio>

#define abs(n) (((n) > 0) ? (n) : (-(n)))
#define max(a, b) ((a) > (b) ? (a) : (b))

int x1, y1, k, x2, y2, l, ans;
int main() {
    scanf("%d %d %d %d %d %d", &x1, &y1, &k, &x2, &y2, &l);
    const int dx = max(k - l, l - 1);
    ans = abs(x2 - x1) / dx + abs(y2 - y1) / dx;
    if ((x2 - x1) % dx) ans++;
    if ((y2 - y1) % dx) ans++;
    printf("%d\n", ans);
}