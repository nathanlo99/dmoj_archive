
#include <stdio.h>
int b, s[100005], e[100005], p[100005], f, t[100005], ans;

int main() {
    scanf("%d", &b);
    for (int i = 0; i < b; i++) scanf("%d %d %d", s + i, e + i, p + i);
    scanf("%d", &f);
    for (int i = 0; i < f; i++) scanf("%d", t + i);
    
    for (int i = 0, j; i < b; i++) {
        ans += p[i];
        for (j = 0; j < f; j++) {
            if (t[j] >= s[i] && t[j] <= e[i]) {
                ans -= p[i];
                break;
            }
        }
    }
    printf("%d\n", ans);
}
