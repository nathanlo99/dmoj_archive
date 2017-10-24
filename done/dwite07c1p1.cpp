#include <cstdio>

int n;
int main() {
    scanf("%d", &n);
    if (n <= 1) { printf("not\n"); return 0; }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) { printf("not\n"); return 0; }
    }
    printf("prime\n");
}