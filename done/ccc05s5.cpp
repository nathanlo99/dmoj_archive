#include <cstdio>
#include <algorithm>

#define MAX 100005
int n, num, grid[MAX];
long long ans, bit[MAX];
std::pair<int, int> scores[MAX];

inline void update(int idx) {
    for (int i = idx; i <= MAX; i += i & -i) {
        bit[i]++;
    }
}

inline long long query(int idx) {
    long long res = 0;
    for (; idx > 0; idx -= idx & -idx) {
        res += bit[idx];
    }
    return res;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &grid[i]);
        scores[i] = std::make_pair(grid[i], i + 1);
    }
    std::sort(scores, scores + n);
    
    // int largest = 0;
    // int largest_value = 0;
    for (int i = 0; i < n; i++) {
        // if (scores[i].first > largest_value) {
        //     largest++;
        //     largest_value = scores[i].first;
        // }
        grid[scores[i].second] = n - i;
    }

    ans = 0;
    update(1);
    for (int i = 1; i <= n; i++) {
        ans += query(grid[i]);
        update(grid[i]);
    }
    printf("%.2lf\n", double(ans) / double(n));
}