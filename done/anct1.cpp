#include <cstdio>

int n, d, ans = 0x3f3f3f3f;
int main() {
    scanf("%d %d", &n, &d);
    if (d < 0) d *= -1;
    for (int i = 0, t; i < n; i++) {
        scanf("%d", &t);
        if (d % t == 0 && d / t < ans) {
            ans = d / t;
        }
    }
    if (ans == 0x3f3f3f3f) printf("This is not the best time for a trip.");
    else printf("%d\n", ans);
}