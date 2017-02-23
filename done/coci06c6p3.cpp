#include <cstdio>
#include <string>
#include <iostream>

int n;
std::string s[31];

int main() {
    scanf("%d ", &n);
    for (int i = 0; i < n; i++) std::getline(std::cin, s[i]);

    // Vertical
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n - 2; y++) {
            if (s[x][y] != '.') {
                if (s[x][y] == s[x][y + 1] && s[x][y + 1] == s[x][y + 2]) {
                    printf("%c\n", s[x][y]);
                    return 0;
                }
            }
        }
    }

    // Horizontal
    for (int x = 0; x < n - 2; x++) {
        for (int y = 0; y < n; y++) {
            if (s[x][y] != '.') {
                if (s[x][y] == s[x + 1][y] && s[x][y] == s[x + 2][y]) {
                    printf("%c\n", s[x][y]);
                    return 0;
                }
            }
                
        }
    }
    
    // Top-to-bottom
    for (int x = 0; x < n - 2; x++) {
        for (int y = 0; y < n - 2; y++) {
            if (s[x][y] != '.') {
                if (s[x][y] == s[x + 1][y + 1] && s[x][y] == s[x + 2][y + 2]) {
                    printf("%c\n", s[x][y]);
                    return 0;
                }
            }
        }
    }

    // Bottom-to-top
    for (int x = 2; x < n; x++) {
        for (int y = 0; y < n - 2; y++) {
            if (s[x][y] != '.') {
                if (s[x][y] == s[x - 1][y + 1] && s[x][y] == s[x - 2][y + 2]) {
                    printf("%c\n", s[x][y]);
                    return 0;
                }
            }
        }
    }

    printf("ongoing\n");
}