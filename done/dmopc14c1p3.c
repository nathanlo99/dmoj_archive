#include <stdio.h>

int N, T, i, tmp;

int main(){
	scanf("%d", &N);
	for(i = 0; i < N; i++){
		scanf("%d", &tmp);
		T += tmp;
	}
	scanf("%d", &tmp);
	for(i = tmp; i--; ){
		scanf("%d", &tmp);
		T += tmp;
		printf("%.3f\n", (double)T/(++N));
	}
	return 0;
}
