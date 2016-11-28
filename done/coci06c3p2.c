#include <stdio.h>
#define abs(x) ((x) > 0 ? (x) : (-(x)))

char s[5];
int ans;

int main() {
    for (int i = 0; i < 4; i++) {
        scanf(" %s ", s);
        for (int j = 0; j < 4; j++) {
            if (s[j] != '.') {
                int k = s[j] - 'A', r = k / 4, c = k % 4;
                ans += abs(i - r) + abs(j - c);
            }
        }
    }
    printf("%d\n", ans);
}