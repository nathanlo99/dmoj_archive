#include <stdio.h>
#include <math.h>

int main() {
	int c, x;
	while (1) {
		scanf("%d", &c);
		if (!c)
			break;
		x = sqrt(c);
		do {
			if (c % x == 0) 
				break;
		}
		while (x-- > 0);
		
		printf("Minimum perimeter is %d with dimensions %d x %d\n", 2 * x + 2 * (c / x), x, c / x);
	}
	return 0;
}