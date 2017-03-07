#include <cstdio>
#include <algorithm>

int n, a[105];
int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    std::sort(a, a + n);
    int lr = (n - 1) / 2, rr = lr + 1;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) printf("%d ", a[lr--]);
        else printf("%d ", a[rr++]);
    }
}