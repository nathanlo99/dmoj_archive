#include <stdio.h>
#include <string.h>

int n, e, i, a, b, p[2000002];

void dfs(int n, int f) {
    if (n == -1) return;
    dfs(p[n], 1);
    if (f) printf("%d ", n);
}

int main() {
    scanf("%d %d %d", &n, &e, &i);
    memset(p, -1, sizeof(p));
    while (e--) {
        scanf("%d %d", &a, &b);
        p[b] = a;
    }
    dfs(i, 0);
}