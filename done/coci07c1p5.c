#include <stdio.h>

int n, m, ans, c, arr[100005][2];
int main() {
    scanf("%d %d", &n, &m);
    c = n;
    arr[c][1]++;
    for (int i = 0, a; i < n; i++) {
        scanf("%d", &a);
        if (a < m) c--;
        else if (a > m) c++;
        ans += arr[c][(i + 1) % 2];
        arr[c][i % 2]++;
    }
    printf("%d\n", ans);
}