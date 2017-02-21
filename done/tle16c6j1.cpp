#include <iostream>
#include <cstdio>

int n, m, q, x, y, t;
int main() {
    scanf("%d %d %d", &n, &m, &q);
    while (q--) {
        scanf("%d %d", &x, &y);
        while (t < x) {
            n--;
            t++;
            if (n < 0) {
                printf("The printer melts at %d second(s).\n", t);
                return 0;
            }
        }
        n += y;
        if (n > m) {
            printf("The printer jams at %d second(s).\n", t);
            return 0;
        }
    }
    printf("The printer melts at %d second(s).\n", t + n + 1);
}