#include <stdio.h>

#define scan(x) while((x=getchar_unlocked())<'0'); for(x-='0';'0'<=(_=getchar_unlocked()); x=(x<<3)+(x<<1)+_-'0');

char _;
int N, Q, cumulative[1000001], current, A, B, i;

int main(){
	scan(N);
	while (N--) {
		scan(current);
		cumulative[i + 1] = cumulative[i] + current;
		i++;
	}
	scan(Q);
	while (Q--) {
		scan(A);
		scan(B);
		printf("%d\n", cumulative[B + 1] - cumulative[A]);
	}
}