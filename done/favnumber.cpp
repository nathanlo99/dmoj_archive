#include <cstdio>
#include <algorithm>

int N, Q, fav[100000], num;

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &fav[i]);
    }
    std::sort(fav, fav + N);
    scanf("%d", &Q);
    while (Q--) {
        scanf("%d", &num);
        const register int* lower = std::lower_bound(fav, fav + N, num);
        const register int* upper = std::upper_bound(fav, fav + N, *lower);
        printf("%d %d\n", *lower, upper - lower);
    }
}