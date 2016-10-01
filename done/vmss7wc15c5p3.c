#include <stdio.h>

int bit[2050][2050], n, k, r, c, t, ans, i1, i2;
int main() {
    scanf("%d", &n);
    while (n--) {
        scanf("%d %d %d %d", &k, &r, &c, &t);
        if (k == 1) {
            i1 = r;
            while (i1 <= r + c) {
                bit[r + c - 1][i1] += t;
                i1 += (i1 & -i1);
            }
        } else {
            i1 = r;
            i2 = r - t - 1;
            while (i1 > 0) {
                ans += bit[r + c - 1][i1];
                i1 -= (i1 & -i1);
            }
            while (i2 > 0) {
                ans -= bit[r + c - 1][i2];
                i2 -= (i2 & -i2);
            }
            ans %= 1000000007;
        }
    }
    printf("%d\n", ans);
}