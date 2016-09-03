#include <stdio.h>

int main(){
    int N, M;
    scanf("%d %d", &N, &M);
    char n[10000][5], a[10000][5];
    for (int i = 0; i < N; i++) scanf("%s", &n[i]);
    for (int i = 0; i < M; i++) {
        scanf("%s", &a[i]);
        for(int j = 0; j < N; j++) printf("%s as %s\n", n[j], a[i]);
    }
}