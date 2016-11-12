#include "stdio.h"
#define mod 1000000007
//#define pow pow_

long long N, A[2001], M, P[2001];

long long pow(long long n, long long p) {
    if (p == 0) return 1;
    if (p & 1) return n * pow((n * n) % mod, p / 2) % mod;
    return pow((n * n) % mod, p / 2) % mod;
}

long long inverse(long long n) {
    return pow(n, mod - 2) % mod;
}

int main() {
	scanf("%lld", &N);
	for (int i = 0; i < N; i++) scanf("%lld", A + i);
	scanf("%lld", &M);

	P[0] = 1;
	for (int i = 1; i < N; i++)
	    P[i] = ((P[i - 1] * (M - 1 + i)) % mod * inverse(i)) % mod;

	for (int i = 0; i < N; i++) {
		long long c = 0;
		for (int j = 0; j <= i; j++)
		    c = (c + P[i - j] * A[j]) % mod;
		printf("%lld ", c);
	}
	printf("\n");
}