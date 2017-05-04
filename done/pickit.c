#include <stdio.h>

int n, a[205], dp[205][205];

int main() {
    while (1) {
        scanf("%d", &n);
        if (n == 0) break;
        for (int i = 0; i < n; i++) scanf("%d", a + i);
        for (int len = 1; len <= n - 2; len++) {
            for (int i = 1; i < n - len; i++) {
                int j = i + len - 1;
                int max = 0;
                for (int k = i; k <= j; k++) {
                    int alt = a[i - 1] + a[k] + a[j + 1] +
                            dp[i][k - 1] + dp[k + 1][j];
                    if (alt > max) max = alt;
                }
                dp[i][j] = max;
            }
        }
        printf("%d\n", dp[1][n - 2]);
    }
}