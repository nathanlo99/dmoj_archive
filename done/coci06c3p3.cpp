#include <cstdio>
#include <set>
#include <cassert>
#include <tuple>
#include <string>
#include <iostream>

int n, ax, ay, bx, by, count;
char c;
std::set<std::pair<int, int> > p;
std::string s;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

int line(int ax, int ay, int bx, int by, int cx, int cy) {
    int dx = bx - ax, dy = by - ay, d = gcd(dx, dy);
    int ex = cx - ax, ey = cy - ay, e = gcd(ex, ey);
    if (dx / d == ex / e && dy / d == ey / e) {
        return 1;
    }
    return 0;
}

int main() {
    scanf("%d ", &n);
    for (int y = 0; y < n; y++) {
        std::getline(std::cin, s);
        for (int x = 0; x < n; x++) {
            if (s[x] != '.') {
                for (std::pair<int, int> a: p) {
                    for (std::pair<int, int> b: p) {
                        std::tie(ax, ay) = a;
                        std::tie(bx, by) = b;
                        if (ax == bx && ay == by) continue;
                        if (line(ax, ay, bx, by, x, y)) {
                            count++;
                        }
                    }
                }
                p.insert(std::make_pair(x, y));
            }
        }
    }
    printf("%d\n", count / 2);
}