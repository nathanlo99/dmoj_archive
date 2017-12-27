#include <cstdio>

int n, m, a;

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i < n; i++) {
        scanf("%d", &a);
        if (a < m) m = a;
    }
    printf("%d\n", m);
}