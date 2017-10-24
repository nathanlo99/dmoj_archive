#include <cstdio>
#include <cmath>

double l, h;
int main() {
    scanf("%lf %lf", &l, &h);
    printf("%d\n", (int)ceil(l * l * h / 3.0));
}