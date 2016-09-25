#include <stdio.h>
#include <stdlib.h>

int n, last_value = 1, ans;
char temp[21], last = ' ';

int main() {
    scanf("%d", &n);
    while (n--) {
        scanf("%s ", temp);
        if (temp[0] == last) {
            last_value++;
            ans += last_value;
        } else {
            ans++;
            last_value = 1;
        }
        last = temp[0];
    }
    printf("%d\n", ans);
    return 0;
}