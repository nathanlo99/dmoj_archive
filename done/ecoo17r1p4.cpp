#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

#define T 10

int n, idx[1005];
std::string s;
std::vector<std::pair<std::string, int> > thing, thing2;

bool vis[1024];

int dfs(int u) {
    if (vis[u]) return 0;
    vis[u] = 1;
    return dfs(thing2[u].second) + 1;
}

int ans;

int getans() {
    int a = 0;
    memset(vis, 0, sizeof(vis));
    std::sort(thing2.begin(), thing2.end());
    for (int i = 0; i < thing2.size(); i++) {
        if (!vis[i]) a += dfs(i) - 1;
    }
    return a;
}

int main() {
    for (int z = 0; z < 10; z++) {
        memset(idx, 0, 1005 * sizeof(int));
        std::cin >> n;
        thing.clear();
        for (int j = 0; j < n; j++) {
            std::cin >> s;
            thing.push_back(std::make_pair(s, j));
        }
        
        if (n == 1) {
            printf("0\n");
            continue;
        }

        int ans = 10000000;
        for (int j = 0; j < n; j++) {
            thing2.clear();
            for (int k = 0; k < n; k++) {
                if (k == j) continue;
                if (k < j) thing2.push_back(std::make_pair(thing[k].first, thing[k].second));
                else thing2.push_back(std::make_pair(thing[k].first, thing[k].second - 1));
            }
            ans = std::min(getans(), ans);
        }
        printf("%d\n", ans);
    }
}