#include <cstdio>

int fib[105], n;

int main() {
    fib[0] = 0; fib[1] = 1;
    for (int i = 2; i <= 100; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    for (int t = 0; t < 5; t++) {
        scanf("%d", &n);
        for (int i = 0; i < 100; i++) {
            if (fib[i] <= n && n < fib[i + 1]) {
                int a = n - fib[i];
                int b = fib[i + 1] - n;
                if (b <= a) printf("%d\n", fib[i + 1]);
                else printf("%d\n", fib[i]);
                break;
            }
        }
    }
}