#include <cstdio>

int t, o, x, w[2], c;
char s[10];

int main() {
    scanf("%d ", &t);
    while (t--) {
        o = x = w[0] = w[1] = c = 0;
        scanf("%s ", s);
        for (int i = 0; i < 9; i++) {
            if (s[i] == 'O') o++;
            else if (s[i] == 'X') x++;
        }
        if (o == x || x - o == 1) {
            if (s[0] != '.' && s[0] == s[1] && s[1] == s[2]) w[s[0] == 'O']++, c++;
            if (s[3] != '.' && s[3] == s[4] && s[4] == s[5]) w[s[3] == 'O']++, c++;
            if (s[6] != '.' && s[6] == s[7] && s[7] == s[8]) w[s[6] == 'O']++, c++;
            if (s[0] != '.' && s[0] == s[3] && s[3] == s[6]) w[s[0] == 'O']++, c++;
            if (s[1] != '.' && s[1] == s[4] && s[4] == s[7]) w[s[1] == 'O']++, c++;
            if (s[2] != '.' && s[2] == s[5] && s[5] == s[8]) w[s[2] == 'O']++, c++;
            if (s[0] != '.' && s[0] == s[4] && s[4] == s[8]) w[s[0] == 'O']++, c++;
            if (s[2] != '.' && s[2] == s[4] && s[4] == s[6]) w[s[2] == 'O']++, c++;
            if (w[0] > 0 && w[1] > 0) {
                printf("no\n");
            } else if (w[0] > 0 && x == o) {
                printf("no\n");
            } else if (w[1] > 0 && x != o) {
                printf("no\n");
            } else {
                printf("yes\n");
            }
        } else {
            printf("no\n");
        }
    }
}