#include "stdio.h"
#include "stdlib.h"
#include "ctype.h"

char A[1000001], B[1000001], c;
int T, i, X, Y;

int p(int a, int b) {
	if (b == 0) return 1;
	if (b == 1) return a;
	int c = p(a, b >> 1);
	if (b % 2 == 1)
		return (a * c * c) % 10;
	return (c * c) % 10;
}

int main(){
	scanf("%s %s", &A, &B);
	while (c = tolower(A[i])) X += p(c - 'a' + 1, ++i);
	X = X % 10 ? X % 10 : 10;
	
	i = 0;
	while (c = tolower(B[i])) Y += p(c - 'a' + 1, ++i);
	Y = Y % 10 ? Y % 10 : 10;
	printf("%d\n", X + Y);
	return 0;
}
