#include <stdio.h>

int main() {
    int N, A, B;
    scanf("%d", &N);
    while (N--) {
        scanf("%d %d", &A, &B);
        printf("%d\n", A + B);
    }
}
