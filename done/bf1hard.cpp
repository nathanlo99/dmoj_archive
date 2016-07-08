#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	int N;
	scanf("%d", &N);
	int list[N];
	
	for(int i = 0; i < N; i++) scanf("%d", list + i);
	sort(list, list + N);
	for(int i = 0; i < N; i++) printf("%d\n", list[i]);

	return 0;
}
