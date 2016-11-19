#include <cstdio>
#define getchar() (*_p?*_p++:(_i[fread(_p=_i,1,4096,stdin)]='\0',*_p++))
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)

char _i[4097], *_p = _i, _, _n;
int _s, _t[11];

inline void print(int a) {
    if (a < 0) putchar_unlocked('-'), a = -a;
    int _ = 0; do { _t[_++] = a % 10; } while (a /= 10);
    while (_--) putchar_unlocked(_t[_]|'0');
    putchar_unlocked('\n');
}

int main() {
    int x;
    // scan(x);
    printf("%d\n", x);
    print(200);
    print(x);
}
