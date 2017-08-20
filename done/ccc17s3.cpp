#include <cstdio>

int n, count[2001], dp[4005], ans, cnt;
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int main() {
    scanf("%d", &n);
    for (int i = 0, a; i < n; i++) {
        scanf("%d", &a);
        count[a]++;
    }

    for (int i = 1; i <= 2000; i++) {
        for (int j = 1; j < i; j++) {
            if (count[i] != 0 && count[j] != 0)
                dp[i + j] += min(count[i], count[j]);
        }
        dp[2 * i] += count[i] / 2;
    }
    for (int i = 2; i <= 4000; i++) {
        if (dp[i] > ans) {
            ans = dp[i];
            cnt = 1;
        } else if (dp[i] == ans) {
            cnt++;
        }
    }
    printf("%d %d\n", ans, cnt); 
}