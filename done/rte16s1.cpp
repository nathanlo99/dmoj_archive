#include <stdio.h>

int t, n, k;
int main() {
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d %d", &n, &k);
        int a = 0, c = 0;
        while (a <= n - k) {
            if (a + c * (c - 1) / 2 > n - k) break;
            a += c * (c - 1) / 2;
            c++;
        }
        printf("%d\n", a);
    }
}