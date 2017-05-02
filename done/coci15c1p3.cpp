#include <cstdio>
#include <set>
using namespace std;

int n, a, ans;
multiset<int> darts;

int main() {
    scanf("%d", &n);
    while (n--) {
        scanf("%d", &a);
        auto itr = darts.find(a);
        if (itr != darts.end()) darts.erase(itr);
        else ans++;
        darts.insert(a - 1);
    }
    printf("%d\n", ans);
}