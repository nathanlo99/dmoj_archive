#include <stdio.h>
#include <math.h>

int main() {
    int N, M, S, T, C;
    scanf("%d", &N);
    while (N--) {
        C = 0;
        scanf("%d %d", &M, &S);
        for (int i = 0; i < M - 1; i++) {
            scanf("%d", &T);
            if (T > S)
                C++;
        }
        printf("Bob wins $%.2f at IOI!\n", sqrt(M - C) * 100.0f);
    }
}
