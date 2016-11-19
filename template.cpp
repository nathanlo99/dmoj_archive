#define getchar() (*_p?*_p++:(_i[fread(_p=_i,1,4096,stdin)]=0,*_p++))
#define scan(x) do{while((x=getchar())<'-');_s=x=='-';if(_s) while((x=getchar())<'0');for(x-='0';'0'<=(_=getchar());x=(x<<3)+(x<<1)+_-'0');x=_s?-x:x;}while(0)

char _i[4097], *_p=_i, _;
int _s;

int main() {
    // Code
}
