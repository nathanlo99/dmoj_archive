#include <cstdio>

int a[5], b[5], n, ans;
int main() {
    for (int t = 0; t < 5; t++) {
        ans = 0;
        for (int i = 0; i < 5; i++) {
            scanf("%d %d", a + i, b + i);
        }
        for (int i = 0; i < 5; i++) {
            scanf("%d", &n);
            if (n == a[i] + b[i]) ans++;
        }
        printf("%d\n", ans);
    }
}