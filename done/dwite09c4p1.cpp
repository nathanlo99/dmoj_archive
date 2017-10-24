#include <cstdio>
#include <cmath>
int n;

int main() {
    for (int i = 0; i < 5; i++) {
        scanf("%d", &n);
        printf("%d\n", (int)round(9000. / n));
    }
}