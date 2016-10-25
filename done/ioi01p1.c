#include <stdio.h>
#define getchar() (*_pinp?*_pinp++:(_inp[fread(_pinp=_inp, 1, 4096, stdin)]='\0', *_pinp++))
#define scan(x) do{while((x=getchar())<'-'); _ssign=x=='-'; if(_ssign) while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0'); x=_ssign?-x:x;}while(0)

char _inp[4097], *_pinp=_inp, _;
int _ssign;

int d, s, x, y, a, l, b, r, t, bit[1025][1025];

inline int query(int x, int y) {
    register int res = 0;
    for (int xx = x; xx > 0; xx -= xx & -xx)
        for (int yy = y; yy > 0; yy -= yy & -yy)
            res += bit[xx][yy];
    return res;
}

int main() {
    scan(d); scan(s);
    for (;;) {
        scan(d);
        switch (d) {
            case 1:
                scan(x); scan(y); scan(a);
                for (int xx = x + 1; xx <= s; xx += xx & -xx) 
                    for (int yy = y + 1; yy <= s; yy += yy & -yy)
                        bit[xx][yy] += a;
                break;
            case 2:
                scan(l); scan(b); scan(r); scan(t);
                printf("%d\n", query(r + 1, t + 1) - query(l, t + 1) - query(r + 1, b) + query(l, b));
                break;
            case 3:
                return 0;
        }
    }
}