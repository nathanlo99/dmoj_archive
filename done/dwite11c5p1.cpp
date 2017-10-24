#include <cstdio>

int d, m, y;
int main() {
    for (int i = 0; i < 5; i++) {
        scanf("%d %d %d", &d, &m, &y);
        long thing = y * 1000000 + m * 1000 + d;
        if (thing <= 1997 * 1000000 + 10 * 1000 + 27) {
            printf("old enough\n");
        } else {
            printf("too young\n");
        }
    }
}