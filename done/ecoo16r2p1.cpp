#include <string>
#include <iostream>

std::string s, s2;
int p[2000005], c, r, m, n, ans, i2;

int main() {
    for (int _ = 0; _ < 10; _++) {
        std::cin >> s;
        s2 = std::string();
        for (int i = 0; i < 2 * s.length() + 1; i++) {
            if (i % 2 == 0) {
                s2 += "|";
            } else {
                s2 += s[i / 2];
            }
            p[i] = 0;
        }
        
        c = 0, r = 0, m = 0, n = 0, ans = 0;
        for (int i = 1; i < s2.length(); i++) {
            if (i > r) {
                p[i] = 0;
                m = i - 1;
                n = i + 1;
            } else {
                i2 = c * 2 - i;
                if (p[i2] < r - i) {
                    p[i] = p[i2];
                    m = -1;
                } else {
                    p[i] = r - i;
                    n = r + 1;
                    m = i * 2 - n;
                }
            }
            while (m >= 0 && n < s2.length() && s2[m] == s2[n]) {
                p[i]++; m--; n++;
            }
            if (p[i] > ans) ans = p[i];
            if (i + p[i] > r) {
                c = i;
                r = i + p[i];
            }
        }
        std::cout << s.length() - ans << std::endl;
    }
}