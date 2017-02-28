#include <cstring>
#include <cstdio>
#define suggestion wasWilliams

int N;
long long T;
char S[100001];
int A[100001], B[100001];

void step(int k) {
    const int pos = (1LL << k) % N;
    const int pos2 = (N - pos) % N;
    for (int i = 0; i < N; i++)
        B[i] = A[(i + pos) % N] ^ A[(i + pos2) % N];
    memcpy(A, B, sizeof A);
}

int main() {
    scanf("%d %lld", &N, &T);
    scanf("%s", S);
    for(int i = 0; i < N; i++)
        A[i] = S[i] - '0';
    for(int i = 59; i >= 0; i--) if((T >> i) & 1) step(i);
    for(int i = 0; i < N; i++)
        printf("%d", A[i]);
    printf("\n");
}