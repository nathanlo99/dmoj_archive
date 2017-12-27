#include <cstdio>

int r, c; // [1, 1000]
int q;    // [1, 1000000]

int x[1005], y[1005];
char s[1005];

int main() {
    scanf("%d %d ", &r, &c);
    for (int i = 0; i < r; i++) {
        scanf("%s ", s);
        for (int j = 0; j < c; j++) {
            if (s[j] == 'X') {
                y[j] = 1;
                x[i] = 1;
            }
        }
    }
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &r, &c);
        printf("%c\n", (y[r - 1] || x[c - 1]) ? 'Y' : 'N');
    }
}