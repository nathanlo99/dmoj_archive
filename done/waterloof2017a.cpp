#include <cstdio>
#include <algorithm>
#include <unordered_set>

using namespace std;

unordered_set<int> triangles;
int n[5];

int main() {
    for (int i = 0; i < 5; i++) scanf("%d", &n[i]);
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            for (int k = j + 1; k < 5; k++) {
                int x = n[i], y = n[j], z = n[k];
                if (z < x + y && x < y + z && y < x + z) triangles.insert(z * 100000000 + y * 10000 + x);
            }
        }
    }
    printf("%lu\n", triangles.size());
}