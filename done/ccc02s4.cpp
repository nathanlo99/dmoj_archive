#include <cstdio>
#include <string>
#include <iostream>

int m, q, cost[102], dp[102], min[102], crit[102], count;
std::string names[102];

int main() {
    scanf("%d %d ", &m, &q);
    for (int i = 1; i <= q; i++) {
        std::getline(std::cin, names[i]);
        scanf("%d ", &cost[i]);
    }
    for (int i = 1; i <= q; i++) {
        dp[i] = dp[i - 1] + cost[i], min[i] = 1;
        int max_cost = -1;
        for (int j = 1; j <= m; j++) {
            if (i - j < 0) continue;
            if (cost[i - j + 1] > max_cost) max_cost = cost[i - j + 1];
            if (dp[i - j] + max_cost < dp[i]) {
                dp[i] = dp[i - j] + max_cost;
                min[i] = j;
            }
        }
    }
    printf("Total Time: %d\n", dp[q]);
    int ptr = q;
    while (ptr) {
        crit[count++] = ptr;
        ptr -= min[ptr];
    }
    for (int i = count - 1; i >= 0; i--) {
        for (int j = crit[i + 1] + 1; j <= crit[i]; j++) {
            printf("%s ", names[j].c_str());
        }
        printf("\n");
    }
}