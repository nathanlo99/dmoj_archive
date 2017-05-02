#include <cstdio>
#include <bitset>
#include <vector>

using namespace std;

vector<int> primes;
bool is_prime[10000005], is_power[10000005];
int totient[1000005], n, done[1000005], ans;

void sieve() {
    for (int i = 0; i < 1000001; i++) {
        is_prime[i] = 1;
        totient[i] = i;
    }
    for (int i = 2; i < 1000000; i++) {
        if (!is_prime[i]) continue;
        primes.push_back(i);
        for (int j = i; j <= 1000000; j += i) {
            is_prime[j] = 0;
            totient[j] = (totient[j] / i) * (i - 1);
        }
    }
}

void sieve2() {
    is_power[1] = 1;
    for (int i = 2; i < 1001; i++) {
        int b = i * i;
        while (b <= 1000000) {
            is_power[b] = 1;
            b *= i;
        }
    }
}

int main() {
    sieve();
    sieve2();
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        const int t = totient[i];
        ans = (ans + is_power[t] * t) % 1000000007;
    }
    printf("%d\n", ans);
}