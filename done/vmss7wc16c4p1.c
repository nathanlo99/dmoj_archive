#include "stdio.h"
#include "math.h"

int A, B;

int main(){
scanf("%d %d", &A, &B);
if (B < 0) { printf("0"); return 0; }
printf("%d\n", (int)(floor(sqrt(B)) - ceil(sqrt(A < 0 ? 0 : A)) + 1));
return 0;
}
