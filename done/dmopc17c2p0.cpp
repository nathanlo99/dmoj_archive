#include <cstdio>

int a, b, c, d, e, f, g;

int main() {
    scanf("%d %d %d %d %d %d %d", &a, &b, &c, &d, &e, &f, &g);
    printf(((((a - e) * (a - e) + (b - f) * (b - f)) <= g * g) ||
                (((c - e) * (c - e) + (d - f) * (d - f)) <= g * g)) ? "Yes\n" : "No\n");
}