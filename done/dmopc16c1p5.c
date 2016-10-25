#include <stdio.h>
#define getchar() (*_pinp?*_pinp++:(_inp[fread(_pinp=_inp, 1, 4096, stdin)]='\0', *_pinp++))
char _inp[4097], *_pinp=_inp;
#define scan(x) do{while((x=getchar())<'-'); _ssign=x=='-'; if(_ssign) while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0'); x=_ssign?-x:x;}while(0)
char _; int _ssign;

#define min(a, b) ((a) < (b) ? (a) : (b))

int n, t, bit[500001];
long long ans, l;

int main() {
    scan(n);
    for (int i = 0; i < n; i++) {
        scan(t);
        l = 0;
        for (int tt = t; tt > 0; tt -= tt & -tt) l += bit[tt];
        ans += min(l, i - l);
        for (; t <= 500001; t += t & -t) bit[t]++;
    }
    printf("%lld\n", ans);
}