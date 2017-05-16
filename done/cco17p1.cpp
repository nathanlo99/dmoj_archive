#include <cstdio>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

int k, n = 1;
vector<int> cycles;
vector<pair<int, int> > edges;

int main() {
    scanf("%d", &k);
    for (int i = 0; i < 5000; i++) {
        cycles.push_back((i * (i - 1)) / 2);
    }
    while (k != 0) {
        int idx = lower_bound(cycles.begin(), cycles.end(), k) - cycles.begin();
        if (cycles[idx] > k) idx--;
        k -= cycles[idx];
        for (int i = 0; i < idx; i++) {
            edges.push_back(make_pair(n + i, n + (i + 1) % idx));
        }
        if (n != 1) edges.push_back(make_pair(1, n));
        n += idx;
    }
    printf("%d %d\n", n - 1, edges.size());
    for (auto v : edges) {
        printf("%d %d\n", v.first, v.second);
    }
}