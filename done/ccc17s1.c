#include <stdio.h>

int n, ans = -1, a[100005], b[100005];
int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n; i++) scanf("%d", &b[i]);
    int ac = 0, bc = 0;
    for (int i = 0; i < n; i++) {
        ac += a[i];
        bc += b[i];
        if (ac == bc) ans = i;
    }
    printf("%d\n", ans + 1);
}