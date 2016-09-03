#include <stdio.h>

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    
    int c = gcd(a, b);
    int n = a / c;
    int d = b / c;
    
    if (n == 0) printf("0");
    else if (d == 1) printf("%d", n);
    else if (n < d) printf("%d/%d", n, d);
    else printf("%d %d/%d", n / d, n % d, d);
}