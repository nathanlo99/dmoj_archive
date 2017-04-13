#include <cstdio>
#include <iostream>
#include <string>

std::string s, a;
int t[1000005], j;

void debug(int i, int j) {
    printf("%d %d\n", i, j);
    for (int x = 0; x < s.size(); x++) {
        printf("%c ", s[x]);
    }
    printf("\n");
    for (int x = 0; x < i; x++) {
        printf("  ");
    }
    printf("^\n");
    for (int x = 0; x < a.size(); x++) {
        printf("%c ", a[x]);
    }
    printf("\n");
    for (int x = 0; x < j; x++) {
        printf("  ");
    }
    printf("^\n\n");
}

int main() {
    std::cin >> s >> a;
    for (int i = 1; i < a.size(); i++) {
        if (a[i] == a[j]) t[i] = ++j;
        else {
            while (a[i] != a[j] && j != 0) j = t[j - 1];
            if (j == 0) t[i] = 0;
            else t[i] = ++j;
        }
    }
    j = 0;
    for (int i = 0; i < s.size(); i++) {
        // debug(i, j);
        if (s[i] == a[j]) { 
            j++; 
            if (j == a.size()) {
                printf("%d\n", i - j + 1);
                return 0;
            }
        } else {
            while (a[j] != s[i] && j != 0) j = t[j - 1];
            if (j != 0) j++;
        }
    }
    printf("-1\n");
}