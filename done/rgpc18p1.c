#include <stdio.h>

int n, a, c;
int main() {
    scanf("%d %d", &n, &a); c = a;
    while (n % c) c++;
    printf("%s %d\n", c == a ? "yes" : "no", c == a ? n / c : c - a);
}