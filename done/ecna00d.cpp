#include <cstdio>

#define N 30
int n, a[N][N][N], bflag;

int main() {
    for(;;) {
		for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) for(int k = 0; k < N; k++) a[i][j][k] = 0;
        scanf("%d", &n);
        if (!n) break;
        if (bflag) printf("\n");
        bflag = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0, b; j <= N; j++) {
                scanf("%d", &b);
                if (!b) break;
                for (int k = 0; k < b; k++) a[i][j][k] = 1;
            }
        }
        for (int i = 0; i < N; i++) {
            int flag = 0;
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    if (!a[j][k][i]) {
                        if (k) {
                            if (flag) printf(" ");
                            printf("%d", k);
                            flag = 1;
                        }
                        break;
                    }
                }
            }
            if (flag) printf("\n");
        }
        printf("\n");

        for (int i = 0; i < N; i++) {
            int flag = 0;
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    if (!a[k][i][j]) {
                        if (k) {
                            if (flag) printf(" ");
                            printf("%d", k);
                            flag = 1;
                        }
                        break;
                    }
                }
            }
            if (flag) printf("\n");
        }
    }
}