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
    for (int i = 0; i < Q; i++) {
        scanf("%d", &num);
        int lower = std::lower_bound(fav, fav + N, num) - fav;
        int upper = std::upper_bound(fav, fav + N, fav[lower]) - fav;
        printf("%d %d\n", fav[lower], upper - lower);
    }
    return 0;
}