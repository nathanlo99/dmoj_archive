#include <cstdio>
#include <vector>
#include <cmath>
#include <cstring>

int n, m, q, bs = 388, ln[150005], tn[150005], a[150005], cycle[150005], bsum[400];
int first[150005][400], last[150005][400], num_blocks, bnum[150005];
std::vector<int> lt[150005];

inline int get(const int i) {
    const int num = ln[i], idx = tn[i], length = lt[num].size();
    const int cycled_index = (idx - cycle[num] + length) % length;
    return a[lt[num][cycled_index]];
}

int main() {
    scanf("%d %d %d", &n, &m, &q);
    memset(first, 0x3f, sizeof(first));
    memset(last, 0x3f, sizeof(last));
    for (int i = 0, l; i < n; i++) {
        scanf("%d", &l);
        l--;
        ln[i] = l;
        tn[i] = lt[l].size();
        lt[l].push_back(i);
        bnum[i] = i / bs;
        if (first[l][i / bs] == 0x3f3f3f3f) first[l][i / bs] = i;
        if (last[l][i / bs] == 0x3f3f3f3f || i > last[l][i / bs]) {
            last[l][i / bs] = i;
        }
        if (i % bs == 0) num_blocks++;
    }
    for (int i = 0, k; i < n; i++) {
        scanf("%d", &k);
        a[i] = k;
        bsum[bnum[i]] += k;
    }
    for (int i = 0, op, l, r; i < q; i++) {
        scanf("%d", &op);
        if (op == 1) {
            scanf("%d %d", &l, &r);
            l--; r--;
            const int lb = bnum[l], rb = bnum[r];
            int ans = 0;
            for (int i = lb; i < rb; i++) ans += bsum[i];
            for (int i = lb * bs; i < l; i++) ans -= get(i);
            for (int i = rb * bs; i <= r; i++) ans += get(i);
            printf("%d\n", ans);
        } else {
            scanf("%d", &l);
            l--;
            int last_index = lt[l][lt[l].size() - 1];
            for (int i = 0; i < num_blocks; i++) {
                if (first[l][i] != 0x3f3f3f3f) {
                    bsum[i] += get(last_index);
                    bsum[bnum[last_index]] -= get(last_index);
                    last_index = last[l][i];
                }
            }
            cycle[l] = (cycle[l] + 1) % lt[l].size();
        }
    }
}