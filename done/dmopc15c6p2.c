#include <stdio.h>
#include <math.h>

int N;
double K, T;

int main() {
	scanf("%d", &N);
	while (N--) {
        scanf("%lf", &K);
		T = fmod(T + K, 360.0);
	}
    printf("%lf", T);
}
