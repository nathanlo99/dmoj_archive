#include <stdio.h>

int m, k, n;

int main() {
    scanf("%d %d %d", &m, &k, &n);
    for (int i = 0; i <= m; i++) {
        if (200 * (i + k) >= 119 * n) {
            printf("%d", i);
            return 0;
        }
    }
    printf("have mercy snew");
}