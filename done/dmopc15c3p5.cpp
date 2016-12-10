#include <cstdio>
#include <unordered_map>

// Thanks quantum
#define getchar() (*_pbuf ? *_pbuf++ : (_buf[fread_unlocked(_pbuf = _buf, 1, 16384, stdin)] = 0, *_pbuf++))
char _buf[16385], *_pbuf = _buf;

static inline int read() {
    int c, o = 0;
    while ((c = getchar()) < '0');
    do o = o*10 + c - '0';
    while ((c = getchar()) >= '0');
    return o;
}

std::unordered_map<long long, int> s;
int n, m, num[36];
long long ans, sum;

static void insert(const long long sum, const int i, const int d) {
    if (!d) s[sum]++, s[sum + num[i]]++;
    else insert(sum, i + 1, d - 1), insert(sum + num[i], i + 1, d - 1);
}

static void insert2(const long long sum, const int i, const int d) {
    if (!d) ans += s[sum] + s[sum - num[i]];
    else insert2(sum, i + 1, d - 1), insert2(sum - num[i], i + 1, d - 1);
}

int main() {
    n = read(), m = read();
    for (int i = 0; i < n; i++) num[i] = read();
    for (int i = 0; i < m; i++) num[n + i] = -read();
    const int mid = (n + m) / 2;
    insert(0, 0, mid - 1);
    insert2(0, mid, n + m - mid - 1);
    printf("%lld\n", ans - 1);
}