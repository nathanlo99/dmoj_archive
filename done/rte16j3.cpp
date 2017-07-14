#include <cstdio>

int bit[1024], co[1024], t, n, c, a, b;
char op;

void update(int a, int amt) {
    for (; a <= 1024; a += a & -a) bit[a] += amt;
}

int query(int a) {
    int res = 0;
    for (; a > 0; a -= a & -a) res += bit[a];
    return res;
}

int query(int a, int b) {
    return query(b) - query(a - 1);
}

int main() {
    scanf("%d ", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d %d ", &n, &c);
        for (int j = 0; j <= n; j++) co[j] = bit[j] = 0;
        for (int j = 0; j < c; j++) {
            scanf("%c", &op);
            switch(op) {
                case 'A':
                    scanf("%d %d ", &a, &b);
                    if (!co[b]) update(b, a);
                    break;
                case 'Q':
                    scanf("%d ", &a);
                    if (co[a]) printf("0\n");
                    else printf("%d\n", query(a, a));
                    break;
                case 'G':
                    scanf("%d ", &a);
                    printf("%d\n", query(1, a));
                    break;
                case 'L':
                    scanf("%d ", &a);
                    printf("%d\n", query(n - a + 1, n));
                    break;
                case 'C':
                    scanf("ovfefe %d ", &a);
                    co[a] = 1;
                    update(a, -query(a, a));
                    break;
                default:
                    printf("BAD: '%c'\n", op);
                    break;
            }
        }
    }
}