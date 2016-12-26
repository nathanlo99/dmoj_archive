#include <stdio.h>

int num[1000000], n, c, a, b, max = -1, max_i = -1;
int main() {
    scanf("%d %d", &n, &c);
    while (c--) {
        scanf("%d %d", &a, &b);
        num[a - 1]++; num[b - 1]++;
    }
    for (int i = 0; i < n; i++) {
        if (num[i] >= max) {
            max = num[i];
            max_i = i;
        }
    }
    printf("%d\n", max_i + 1);
}