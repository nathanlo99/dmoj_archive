#include <cstdio>
#include <vector>
#define mod 1000000007
#define M mod
long long n, par[100005], f[100005], size[100005];
std::vector<long long> children[100005];

long long inv(int i)
{
    long long out=1;
    while (i>1) {
        int t=M/i+1;
        i=(i*t-M);
        out=(out*t)%M;
    }
    return out;
}

void get_size(long long n) {
    size[n] = 1;
    for (long long a: children[n]) {
        get_size(a);
        size[n] += size[a];
    }
}

long long get_ans(long long n) {
    if (children[n].empty()) return 1;
    long long res = f[size[n] - 1];
    for (long long a : children[n]) {
        res = (res * inv(f[size[a]])) % mod;
        res = (res * get_ans(a)) % mod;
        res = (res + mod) % mod;
    }
    return res;
}

int main() {
    f[0] = 1;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", par + i);
        children[par[i]].push_back(i + 1);
        f[i + 1] = f[i] * (i + 1) % mod;
    }
    get_size(0);
    printf("%lld\n", get_ans(0));
}