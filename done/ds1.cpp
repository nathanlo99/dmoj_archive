#include <cstdio>

long long nums[100001], sum_bit[100001], freq_bit[100001];
int n, m, a, b;

char c;

void update (long long* bit, int idx, long long value) {
    while (idx <= 100000) {
        bit[idx] += value;
        idx += (idx & -idx);
    }
}

long long query(long long* bit, int idx) {
    long long res = 0;
    while (idx > 0) {
        res += bit[idx];
        idx -= (idx & -idx);
    }
    return res;
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%lld", &nums[i]);
        update(sum_bit, i, nums[i]);
        update(freq_bit, nums[i], 1);
    }

    while (m--) {
        do {
            c = getchar();
        } while (!(c == 'C' || c == 'S' || c == 'Q'));
        
        if (c == 'C') {
            scanf("%d %d", &a, &b);
            update(sum_bit, a, b - nums[a]);
            update(freq_bit, b, 1);
            update(freq_bit, nums[a], -1);
            nums[a] = b;
        } else if (c == 'Q') {
            scanf("%d", &a);
            printf("%lld\n", query(freq_bit, a));
        } else { // c == 'S'
            scanf("%d %d", &a, &b);
            printf("%lld\n", query(sum_bit, b) - query(sum_bit, a - 1));
        }
    }
}