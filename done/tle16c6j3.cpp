#include <cstdio>

#define abs(n) (((n) > 0) ? (n) : (-(n)))
#define max(a, b) ((a) > (b) ? (a) : (b))

int x1, y1, k, x2, y2, l;
int main() {
    scanf("%d %d %d %d %d %d", &x1, &y1, &k, &x2, &y2, &l);
    int dx = max(k - l, l - 1);
    int x = abs(x2 - x1) / dx, y = abs(y2 - y1) / dx;
    if ((x2 - x1) % dx) x++;
    if ((y2 - y1) % dx) y++;
    printf("%d\n", x + y);
}