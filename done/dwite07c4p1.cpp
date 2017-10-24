#include <cstdio>
#include <cmath>

#define PI 3.1415926535897
int a, b;
int main() {
    for (int t = 0; t < 5; t++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", (int)round(b * b / 9.81 * sin(2 * a * PI / 180.)));
    }
}