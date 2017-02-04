#include <cstdio>
#include <vector>

int n, m, pos[1000002]; std::vector<int> lis;
int main() {
    for (int i = 0; i < 1000002; i++) pos[i] = -1;
    scanf("%d", &n);
    for (int i = 0, x = 0; i < n; i++) {
        scanf("%d ", &x); pos[x] = i;
    }
    scanf("%d ", &m);
    for (int i = 0, x = 0; i < m; i++) {
        scanf("%d", &x);
        if (pos[x] < 0) continue;
        if (lis.empty() || pos[x] > lis.back()) {
            lis.push_back(pos[x]);
        } else {
            int p = std::lower_bound(lis.begin(), lis.end(), pos[x]) - lis.begin();
            lis[p] = pos[x];
        }
    }
    printf("%d\n", lis.size());
}