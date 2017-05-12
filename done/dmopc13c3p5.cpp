#include <cstdio>
#define maxx(a, b) ((a) > (b) ? (a) : (b))

int m, u, r, v, t, f, dp[155][305][105];

int main() {
    scanf("%d %d %d ", &m, &u, &r);
    for (int i = 1; i <= r; i++) {
        scanf("%d %d %d ", &v, &t, &f);
        for (int time = 0; time <= m; time++)
            for (int food = 0; food <= u; food++)
                dp[i][time][food] = dp[i - 1][time][food];

        for (int time = 0; time + t <= m; time++) {
            for (int food = 0; food + f <= u; food++) {
                dp[i][time + t][food + f] = maxx(dp[i - 1][time + t][food + f],
                                        dp[i - 1][time][food] + v);
            }
        }
    }
    printf("%d\n", dp[r][m][u]);
}