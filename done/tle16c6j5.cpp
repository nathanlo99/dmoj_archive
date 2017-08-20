#include <vector>
#include <map>

int n, num[3], cost, min_cost, ans, cnt, poss[2005][2005];
std::vector<int> costs[3];

int main() {
    scanf("%d %d %d %d", &n, num, num + 1, num + 2);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < num[i]; j++) {
            scanf("%d", &cost);
            if (cost <= n) costs[i].push_back(cost);
        }
    }
    
    for (const int c : costs[0]) {
        poss[0][c] = 1;
        if (c > ans) ans = c, cnt = 1;
    }

    bool flag = 1;
    for (int i = 1; flag && i < 2005; i++) {
        flag = 0;
        for (const int j : costs[i % 3]) {
            for (int k = 0; k < 2005; k++) {
                if (poss[i - 1][k] == 0) continue;
                const int alt = k + j, count = poss[i - 1][k];
                if (alt > n) continue;
                flag = 1;
                if (alt > ans) ans = alt, cnt = count;
                else if (alt == ans) cnt = (cnt + count) % 1000000007;
                poss[i][alt] = (poss[i][alt] + count) % 1000000007;
            }
        }
    }

    printf("%d %d\n", cnt % 1000000007, n - ans);
    
}