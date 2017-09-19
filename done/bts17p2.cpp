#include <cstdio>

double ans = 1.0;
int n, a, b;

int main() {
    scanf("%d", &n);
    while (n--) {
        scanf("%d %d", &a, &b);
        ans *= (double)(b - a) / b;
    }
    printf("%.6lf\n", ans);
}