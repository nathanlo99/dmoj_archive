long long lower(long long lo, long long hi, int val) {
    if (lo == hi) return lo;
    long long f = 0;
    const long long p = lo + (hi - lo) / 2;
    for (long long i = 5; i <= p; i *= 5) f += p / i;
    if (f >= val) return lower(lo, lo + (hi - lo) / 2, val);
    return lower(lo + (hi - lo) / 2 + 1, hi, val);
}

long long a, b;
int main() {
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", lower(1, 10000000000LL, b + 1) - lower(1, 10000000000LL, a));
}