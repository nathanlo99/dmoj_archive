#include <stdio.h>

int n;

int good(int n) {
    while (n > 0) {
        if (n % 10 == 0) return 0;
        n /= 10;
    }
    return 1;
}

int main() {
    scanf("%d", &n);
    n++;
    while (!good(n)) n++;
    printf("%d\n", n);
}