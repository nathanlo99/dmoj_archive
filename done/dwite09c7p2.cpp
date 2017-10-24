#include <cstdio>

int n, ans;

int prime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    for (int t = 0; t < 5; t++) {
        scanf("%d", &n);
        ans = 0;
        for (int i = 0; i <= n; i++) {
            if (prime(i)) ans += i;
        }
        printf("%d\n", ans);
    }
}