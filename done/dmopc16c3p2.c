#include <stdio.h>

long long n, k, d, a, t, p[100000], s[100000];
char c;

int main() {
    scanf("%lld %lld %lld", &n, &k, &d);
    while (n--) {
        scanf(" %c", &c);
        if (c == 'T') {
            p[t] = 1;
            t++;
        } else {
            scanf("%lld", &a);
            if (t > 0 && p[t - 1] < d) {
                p[t - 1] *= a;
            }
        }
    }
    a = 1;
    int tt = 0;
    for (int i = t - 1; i >= 0; i--) {
        if (p[i] > d || a == -1) a = -1;
        else {
            a *= p[i];
            if (a > d) a = -1;
        }
        s[tt++] = a;
    }

    for (int i = t - 1; i >= 0; i--) {
        if (s[i] == -1 || s[i] > d) {
            printf("dust\n");
        } else {
            printf("%lld\n", s[i]);
        }
    }


}