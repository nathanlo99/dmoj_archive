#include <stdio.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

int n, t[4];
int cur[16], last[16];
int dp[16][100005];

int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d %d %d %d", t + 0, t + 1, t + 2, t + 3);
        for (int j = 0; j < 16; j++) cur[j] = last[j];
        for (int a = 0; a < 4; a++) {
            if (t[a] != -1) {
                for (int j = 0; j < 16; j++) {
                    if ((j >> a) & 1) {
                        cur[j] = max(cur[j], 
                                last[j ^ (1 << a)] + t[a]);
                    }
                }
            }
        }
        for (int i = 0; i < 16; i++) last[i] = cur[i];
    }
    printf("%d\n", last[15]);
}