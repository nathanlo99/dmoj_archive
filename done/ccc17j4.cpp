#include <cstdio>

int d, h, m, ans;
int main() {
    scanf("%d", &d);
    ans += 31 * (d / 720);
    d %= 720;
    h = 12, m = 0;
    for (int i = 0; i <= d; i++) {
        if (h >= 10) {
            int a = 1, b = h % 10, c = m / 10, d = m % 10;
            if (a - b == b - c && b - c == c - d) ans++;
        } else {
            int b = h % 10, c = m / 10, d = m % 10;
            if (b - c == c - d) ans++;
        }
        m++;
        if (m == 60) h++, m = 0;
        if (h == 13) h = 1;
    }
    printf("%d\n", ans);
}