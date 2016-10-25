#include <cstdio>
#include <algorithm>

#define getchar() (*_pinp?*_pinp++:(_inp[fread(_pinp=_inp, 1, 4096, stdin)]='\0', *_pinp++))
#define scan(x) do{while((x=getchar())<'-'); _ssign=x=='-'; if(_ssign) while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0'); x=_ssign?-x:x;}while(0)

char _inp[4097], *_pinp=_inp, _;
int _ssign;

int N;
int list[100000];

int main(){
	scan(N);
	for(int i = 0; i < N; i++) scan(list[i]);
	std::sort(list, list + N);
	for(int i = 0; i < N; i++) printf("%d\n", list[i]);
}