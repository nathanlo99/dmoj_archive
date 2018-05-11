#include <stdio.h>

void do_thing() {
    int p = 0;
    for (int i = 0; i < 5; i++) {
        if (getchar() == '*') { p = i; }
    }
    getchar();
    for (int i = 0; i < 5; i++) {
        char c = getchar(); getchar();
        if (c == 'R' && p < 4) p++;
        else if (c == 'L' && p > 0) p--;
    }
    for (int i = 0; i < 5; i++) {
        printf("%c", (i == p) ? '*' : '.');
    }
    printf("\n");
}

int main() {
    for (int i = 0; i < 5; i++) do_thing();
}