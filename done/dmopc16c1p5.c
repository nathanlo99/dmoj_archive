#include <stdio.h>

#define min(a, b) ((a) < (b) ? (a) : (b))

int n, t, bit[500001], l;
long long ans;

void update(int idx) {
    for (; idx <= 500001; idx += idx & -idx) bit[idx]++;
}

long long query(int idx) {
    long long res = 0;
    for (; idx > 0; idx -= idx & -idx) res += bit[idx];
    return res;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &t);
        l = query(t);
        update(t);
        ans += min(l, i - l);
    }
    printf("%lld\n", ans);

}