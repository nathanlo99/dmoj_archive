#include <stdio.h>
#include <string.h>

char number[52], cache[52], *print;
int n, p, mp, a, b;

int main() {
    scanf("%d", &n);
    while (n--) {
        memset(number, 0, sizeof(number));
        memset(cache, 0, sizeof(number));
        scanf("%s", number);
        p = strlen(number) - 1;
        strcpy(cache, number);
        printf("%s\n", number);
        while (p > 1) {
            a = number[p] - '0';
            number[p] = 0;
            for (mp = p - 1; mp >= 0; mp--) {
                b = number[mp] - '0';
                if (b >= a) {
                    number[mp] = b - a + '0';
                    break;
                } else {
                    number[mp] = 10 + b - a + '0';
                    a = 1;
                }
            }
            print = number;
            while (*print == '0') print++;
            printf("%s\n", print);
            if (strlen(print) <= 2) break;
            p--;
        }
        if (number[0] == number[1]) {
            printf("The number %s is divisible by 11.\n\n", cache);
        } else {
            printf("The number %s is not divisible by 11.\n\n", cache);
        }
    }
}