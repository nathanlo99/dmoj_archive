
#include <cstdio>

int n, d, x, y, lx, ly, streak, ans;
int main() {
    scanf("%d %d", &n, &d);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x, &y);
        if (i == 0 || (x - lx) * (x - lx) + (y - ly) * (y - ly) <= d * d) {
            streak++;
            if (streak > ans) ans = streak;
        } else {
            streak = 0;
        }
        lx = x; ly = y;
    }
    printf("%d\n", ans);
}

