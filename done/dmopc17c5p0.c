#include <stdio.h>

int b, p, i;
char c;

int main() {
    scanf("%d %d %c", &b, &p, &c);
    printf((b < 2 * p) ? "NO PIZZA" : "%c\n", 'A' + 2 * (b < 5 * p) + (c == 'Y'));
}