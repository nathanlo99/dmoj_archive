#include <stdio.h>

int n, m, par[100002];

int root(int n) {
    if (par[n] != n) par[n] = root(par[n]);
    return par[n];
}

void merge(int a, int b) {
    int ar = root(a), br = root(b);
    if (ar != br) par[ar] = br;
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i <= n; i++) par[i] = i;

    for (int i = 0, a, b, c; i < m; i++) {
        scanf("%d %d", &a, &b);
        for (int j = 1; j < a; j++) {
            scanf("%d", &c);
            merge(b, c);
        }
    }
    int r1 = root(1);
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (root(i) == r1) ans++;
    }
    printf("%d\n", ans);
    for (int i = 1; i <= n; i++) {
        if (par[i] == r1) printf("%d ", i);
    }
}