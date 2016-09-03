#include <stdio.h>

#define scan(x) do{while((x=getchar_unlocked())<'0'); for(x-='0';'0'<=(_=getchar_unlocked()); x=(x<<3)+(x<<1)+_-'0');}while(0)

char _;
int N, Q, masses[1000001], cumulative[1000001], C, current, A, B;

int main(){
	scan(N);
	for (int i = 0; i < N; i++){
		scan(current);
		C += current;
		cumulative[i + 1] = C;
	}
	scan(Q);
	for (int i = 0; i < Q; i++){
		scan(A);
		scan(B);
		printf("%d\n", cumulative[B + 1] - cumulative[A]);
	}
	return 0;
}