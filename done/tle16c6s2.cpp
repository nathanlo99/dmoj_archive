#include <cstdio>
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

float ax, ay, bx, by;
float ans;
int main() {
    scanf("%f %f %f %f", &ax, &ay, &bx, &by);
    if (ax > bx && ay > by) {
        // ax, ay is the outside point
        ans = ax * ay * 2;
    } else if (bx > ax && by > ay) {
        ans = bx * by * 2;
    } else if (ax == bx) {
        if (ay > by) ans = ax * ay * 2;
        else ans = bx * by * 2;
    } else if (ay == by) {
        if (ax > bx) ans = ax * ay * 2;
        else ans = bx * by * 2;
    } else {
        float m = (by - ay) / (bx - ax);
        float b = by - m * bx;
        float a = -b / m;
        ans = a * b / 2;
        if (ax > bx) {
            if (a > 2 * ax) ans = min(ans, ax * ay * 2);
            if (b > 2 * by) ans = min(ans, bx * by * 2);
        } else {
            if (a > 2 * bx) ans = min(ans, bx * by * 2);
            if (b > 2 * ay) ans = min(ans, ax * ay * 2);
        }
    }
    printf("%.6lf\n", ans);
}