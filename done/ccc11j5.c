#include <stdio.h>

int dp[7] = {1, 1, 1, 1, 1, 1, 1};
int N, A;

int main() {
    scanf("%d", &N);
    for (int i = 1; i < N; i++) {
        scanf("%d", &A);
        dp[A] *= 1 + dp[i];
    }
    printf("%d\n", dp[N]);
    return 0;
}