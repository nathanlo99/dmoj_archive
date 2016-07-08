#include <stdio.h>

int n;
long long a, b, p;
int main() {
	scanf("%d", &n);
	while(n--){
		scanf("%lld %lld %lld", &a, &b, &p);
		if(a * b != p) printf("16 BIT S/W ONLY\n");
		else printf("POSSIBLE DOUBLE SIGMA\n");
	}
}
