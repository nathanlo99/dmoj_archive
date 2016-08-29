#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

int N, Q, T[64], T1[64], L, B;
std::vector<int> sets[1001];

int main() {
    scanf("%d %d", &N, &Q);
    for (int i = 1; i <= N; i++) {
        scanf("%d", &L);
        for (int j = 0; j < L; j++) {
            scanf("%d", &B);
            sets[i].push_back(B);
        }
        std::sort(sets[i].begin(), sets[i].end());
    }
    for (int i = 0; i < Q; i++) {
        scanf("%d", &L);
        if (L == 0) {
            printf("0\n");
            continue;
        }

        int len = 0, *X = T, *Y = T1, *Z;
        for (int i = 0; i < L; i++) {
            scanf("%d", &B);
            len = std::set_symmetric_difference(Y, Y + len, sets[B].begin(), sets[B].end(), X) - X;
            Z = X;
            X = Y;
            Y = Z;
        }
        printf("%d ", len);
        std::sort(Y, Y + len);
        for (int i = 0; i < len; i++) {
            printf("%d ", Y[i]);
        }
        printf("\n");
        memset(T, 0, sizeof(T));
        memset(T1, 0, sizeof(T1));
        
    }
}