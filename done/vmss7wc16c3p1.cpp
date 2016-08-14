#include <cstdio>
#define MIN(a, b) a > b ? b : a
#define MAX(a, b) a > b ? a : b

int X1, Y1, X2, Y2, N, X, Y;
int main() {
  scanf("%d", &N);
  scanf("%d %d", &X1, &Y1);
  X2 = X1;
  Y2 = Y1;
  N--;
  while (N--) {
    scanf("%d %d", &X, &Y);
    X1 = MIN(X1, X);
    Y1 = MIN(Y1, Y);
    X2 = MAX(X2, X);
    Y2 = MAX(Y2, Y);
  }
  printf("%d", (X2 - X1) * (Y2 - Y1));
}
