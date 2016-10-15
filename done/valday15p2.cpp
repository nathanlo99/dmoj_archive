#include <cstdio>

int c, m, v, w, dp[1001];

int main() {
    scanf("%d %d", &c, &m);
    while (c--) {
        scanf("%d %d", &v, &w);
        for (int i = m; i >= w; i--)
            if (dp[i - w] + v > dp[i])
                dp[i] = dp[i - w] + v;
    }
    printf("%d\n", dp[m]);
}