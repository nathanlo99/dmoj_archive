#include <cstdio>
#include <string>
#include <iostream>

int n;
std::string a, t, c, s;

inline int index(char c) {
    if (c == '_') return 26;
    else return c - 'A';
}

int main() {
    for (int i = 0; i < 27; i++) {
        std::getline(std::cin, a);
        t += a;
    }
    c = std::string(t);
    scanf("%d ", &n);
    n = (n - 1) % (27 * 2 * 5 * 7 * 11 * 13);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 27; j++) {
            t[j] = c[index(t[j])];
        }
    }
    std::getline(std::cin, s);
    for (int i = 0; i < s.length(); i++) {
        printf("%c", t[index(s[i])]);
    }
    printf("\n");
}