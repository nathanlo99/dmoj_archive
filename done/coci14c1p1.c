#include <stdio.h>
int N, last = 0, temp;

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d ", &temp);
        temp *= (i + 1);
        printf("%d ", temp - last);
        last = temp;
    }
}