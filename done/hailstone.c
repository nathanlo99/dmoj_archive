#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int c = 0;
    while (n != 1) {
        n = (n % 2 == 0) ? (n / 2): (3 * n + 1);
        c++;
    }
    printf("%d", c);
}
