#include <stdio.h>

unsigned long long a, b, c;

int main() {
    scanf("%llu %llu %llu", &a, &b, &c);
    printf("%llu\n", (a + b + c) % 42069900169420);
}