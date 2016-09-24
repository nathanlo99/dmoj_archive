#include <stdio.h>

#define max(a, b) (a > b ? a : b)

int n;
long long x, sum, ans;
int main() {
  scanf("%d", &n);
  while (n--) {
    scanf("%lld", &x);
    sum += x;
    ans = max(ans, x);
  }

  printf("%lld\n", max(2 * ans, sum));
}