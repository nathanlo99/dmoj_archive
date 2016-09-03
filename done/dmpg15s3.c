#define solution isJasons
#include <stdio.h>

int n, m, t1, t2, a[100000], b[100000], c[100000];
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    b[i] = c[i] = 0;
  }
  scanf("%d", &m);
  while (m--) {
    scanf("%d%d", &t1, &t2);
    b[t1] = -t2;
  }
  b[0] = a[0];
  for (int i = 1; i < n; i++) {
    b[i] += b[i - 1] + a[i];
    if (b[i] < c[i - 1] + a[i])
      b[i] = c[i - 1] + a[i];
    c[i] = c[i - 1] > b[i - 1] ? c[i - 1] : b[i - 1];
  }
  printf("%d", b[n - 1] > c[n - 1] ? b[n - 1] : c[n - 1]);
}