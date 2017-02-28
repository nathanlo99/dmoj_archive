#include <cstdio>
#define maxn 105 * 1005
#define min(a, b) ((a) < (b) ? (a) : (b))

int ans = 0x3f3f3f3f, n, b, dp[maxn], dp2[maxn];
int main() {
    scanf("%d", &n);
    dp[0] = dp2[0] = 1;
    for (int i = 0, a; i < n; i++) {
        scanf("%d", &a);
        for (int j = maxn; j >= a; j--) {
            if (dp[j - a]) {
                if (!dp[j]) dp[j] = dp[j - a] + 1;
                else dp[j] = min(dp[j], dp[j - a] + 1);
            }
        }
    }
    scanf("%d", &b);
    for (int i = 0, a; i < b; i++) {
        scanf("%d", &a);
        for (int j = maxn; j >= a; j--) {
            if (dp2[j - a]) {
                if (!dp2[j]) dp2[j] = dp2[j - a] + 1;
                else dp2[j] = min(dp2[j], dp2[j - a] + 1);
                if (dp[j] != 0 && dp[j] + dp2[j] < ans) {                               ans = dp[j] + dp2[j];
                }
            }
        }
    }
    if (ans == 0x3f3f3f3f) printf("impossible");
    else printf("%d\n", ans - 2);
}