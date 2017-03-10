#include <cstdio>
#include <vector>

int n, a, b, x, last, names[101], max = -1, ans;
std::vector<int> c;
#define abs(a) (((a) > 0) ? (a) : (-(a)))

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d ", &x);
        names[i] = x;
        for (int j = 0; j <= i; j++) {
            int alt = (x + names[j]) / 2;
            if (alt % 2 == 0) {
                c.push_back(alt + 1);
                c.push_back(alt - 1);
            } else {
                c.push_back(alt);
            }
        }
    }
    scanf("%d %d", &a, &b);
    if (a % 2 == 0) a++;
    if (b % 2 == 0) b--;
    c.push_back(a), c.push_back(b);
    for (int q: c) {
        if (q < a || q > b) continue;
        // printf("%d: ", q);
        int closest = 0x3f3f3f3f;
        for (int i = 0; i < n; i++) {
            if (abs(q - names[i]) < closest) {
                closest = abs(q - names[i]);
            }
        }
        if (closest > max) {
            max = closest;
            ans = q;
        }
        // printf("%d\n", closest);
    }
    printf("%d\n", ans);
}