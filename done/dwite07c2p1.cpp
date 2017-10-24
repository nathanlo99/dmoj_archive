#include <cstdio>

int n;

int prime(int n) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int semiprime(int n) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return prime(n / i);
        }
    }
    return 0;
}

int main() {
    for (int t = 0; t < 5; t++) {
        scanf("%d", &n);
        printf("%s\n", semiprime(n) ? "semiprime" : "not");
    }
}