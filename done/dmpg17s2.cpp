#include <cstdio>

int n, m, a, b;
int par[100005];
char op;

int parent(int n) {
    if (par[n] != n) par[n] = parent(par[n]);
    return par[n];
}

int main() {
    scanf("%d %d ", &n, &m);
    for (int i = 0; i < 100005; i++) par[i] = i;
    for (int i = 0; i < m; i++) {
        op = getchar();
        scanf("%d %d ", &a, &b);
        int pa = parent(a);
        int pb = parent(b);
        if (op == 'A') {
            par[pa] = pb;
        } else {
            printf((pa == pb) ? "Y\n" : "N\n");
        }
    }
}