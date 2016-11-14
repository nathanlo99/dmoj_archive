#include <cstdio>
#include <algorithm>

int n, num, grid[100005];
long long ans, bit[100005];
std::pair<int, int> scores[100005];

inline int readint() {
    int c, o = 0;
    while ((c = getchar_unlocked()) > '9' || c < '0');
    do {
        o = (o << 3) + (o << 1) + c - '0';
    } while ((c = getchar_unlocked()) <= '9' && c >= '0');
    return o;
}

int main() {
    n = readint();
    for (int i = 0; i < n; i++) {
        grid[i] = readint();
        scores[i] = std::make_pair(grid[i], i + 1);
    }
    std::sort(scores, scores + n);
    
    for (int i = 0; i < n; i++) grid[scores[i].second] = n - i;

    ans = 0;
    for (int j = 1; j <= 100005; j += j & -j) bit[j]++;
    for (int i = 1; i <= n; i++) {
        for (int j = grid[i]; j > 0; j -= j & -j) ans += bit[j];
        for (int j = grid[i]; j <= 100005; j += j & -j) bit[j]++;
    }
    printf("%.2lf\n", double(ans) / double(n));
}