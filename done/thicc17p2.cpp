#include <cstdio>

#define mod 1000000007

long long a, b, m, n;
long long sum, square_sum;
int main() {
	scanf("%lld %lld %lld %lld", &n, &a, &b, &m);
	while (n--) {
		sum += a; square_sum += a * a;
		sum %= mod; square_sum %= mod;
		a = (a * b) % m;
	}
	printf("%lld\n", (sum * sum - square_sum) % mod);
}