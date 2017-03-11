#include <cstdio>

int n, m, ans, c, odd[100005], even[100005];
int main() {
    scanf("%d %d", &n, &m);
    c = n;
    odd[c]++;
    for (int i = 0, a; i < n; i++) {
        scanf("%d", &a);
        if (a < m) {
            c--;
        } else if (a > m) {
            c++;
        }
        if (i % 2 == 0) {
            ans += odd[c];
            even[c]++;
        } else {
            ans += even[c];
            odd[c]++;
        }
        // printf("%d\n", c);
    }
    printf("%d\n", ans);
}