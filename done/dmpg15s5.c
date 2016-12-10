#include <stdio.h>

// Thanks quantum
#define getchar() (*_pbuf ? *_pbuf++ : (_buf[fread_unlocked(_pbuf = _buf, 1, 16384, stdin)] = 0, *_pbuf++))
char _buf[16385], *_pbuf = _buf;

int read() {
    int c, o = 0;
    while ((c = getchar()) < '0');
    do o = o*10 + c - '0';
    while ((c = getchar()) >= '0');
    return o;
}

char d[10002][10002];
int n, m, x, y, w, h, ans;

int main() {
    n = read(); m = read();
    while (m--) {
        x = read(); y = read(); w = read(); h = read();
        d[x + w + 1][y + h + 1]++; d[x + 1][y + 1]++;
        d[x + w + 1][y + 1]--; d[x + 1][y + h + 1]--;
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            d[i][j] += d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1];
            ans += d[i][j] & 1;
        }
    }

    printf("%d\n", ans);
}