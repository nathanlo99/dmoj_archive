#include <cstdio>

int n, bad;
char c;

int main() {
    for (int i = 0; i < 5; i++) {
        bad = 0;
        while (!bad && (c = getchar()) != '\n' && c != EOF) {
            if (c == '-') n--;
            else n++;
            if (n < 0) {
                printf("OH NOES!\n");
                while (c != '\n' && c != EOF) c = getchar();
                n = 0;
                bad = 1;
            }
        }
        if (!bad) printf("%d\n", n); 
    }
}