#include <stdio.h>

int N, T, S;
int main() {
    scanf("%d", &N);
    while (N--) {
        scanf("%d", &T);
        S ^= T;
    }
    printf("%d\n", S);
}