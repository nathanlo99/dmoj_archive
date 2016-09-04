#include <stdio.h>
#include <math.h>

int N;
int s, x;
double t, height;
int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d %d %lf", &s, &x, &t);
		height += t * s * sin(x * 3.1415926535 / 180.0);
	}
	printf("%d\n", (int)round(sqrt(19.6 * height)));
}