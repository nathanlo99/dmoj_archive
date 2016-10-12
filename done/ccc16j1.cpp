#include <cstdio>
#include <queue>

int wins;
char result;

int main() {
    for (int i = 0; i < 6; i++) {
        scanf(" %c", &result);
        if (result == 'W') {
            wins++;
        }
    }
    if (wins >= 5) {
        printf("1\n");
    } else if (wins >= 3) {
        printf("2\n");
    } else if (wins >= 1) {
        printf("3\n");
    } else {
        printf("-1\n");
    }
}