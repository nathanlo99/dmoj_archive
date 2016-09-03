#include <cstdio>
#include <algorithm>

int N;
int list[100000];

int main(){
	scanf("%d", &N);
	for(int i = 0; i < N; i++) scanf("%d", list + i);
	std::sort(list, list + N);
	for(int i = 0; i < N; i++) printf("%d\n", list[i]);
}