#include <stdio.h>

// Still don't know how this works.
long long n, k, p, ans;
int main() {
    scanf("%lld %lld", &n, &k);
    p = 1;
    while (p < n) {
        ans++;
        p += (p < k ? p : k);
        if (p >= k) {
            if ((n - p) % k == 0)
                ans--;
            ans += (n - p) / k + 1;
            break;
        }
    }
    printf("%lld", ans);
}