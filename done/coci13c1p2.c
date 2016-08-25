#include <stdio.h>

int a, b, r = 0;

int main() {
    scanf("%d %d", &a, &b);
    for (int i = 0; i < b; i++) {
        if ((i * a) % b)
            r++;
    }
    printf("%d", r);
}