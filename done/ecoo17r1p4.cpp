#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

#define min(a, b) ((a) < (b) ? (a) : (b))

int n;
std::string s;
std::vector<std::pair<std::string, int> > a, b;

bool vis[1024];

int main() {
    for (int z = 0; z < 10; z++) {
        std::cin >> n;
        a.clear();
        for (int j = 0; j < n; j++) {
            std::cin >> s;
            a.push_back(std::make_pair(s, j));
        }
        
        if (n == 1) {
            printf("0\n");
            continue;
        }

        int ans = 10000000;
        for (int j = 0; j < n; j++) {
            b.clear();
            memset(vis, 0, sizeof(vis));
            for (int k = 0; k < n; k++) {
                if (k != j) b.push_back(std::make_pair(a[k].first, a[k].second - (k > j)));
            }
            std::sort(b.begin(), b.end());
            
            int t = n - 1;
            for (int i = 0; i < b.size(); i++) {
                if (!vis[i]) {
                    int u = i;
                    while (!vis[u]) {
                        vis[u] = 1;
                        u = b[u].second;
                    }
                    t--;
                }
            }
            ans = min(t, ans);
        }
        printf("%d\n", ans);
    }
}