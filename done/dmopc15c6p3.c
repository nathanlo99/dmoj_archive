#include <stdio.h>

long long diff[200002], value[200002], sum[200002], K;
int N, M, A, B;

int main() {
  scanf("%d %d %lld", &N, &M, &K);
  if (K == 0) {
    printf("0\n");
    return 0;
  }
  for (int i = 0; i < M; i++) {
    scanf("%d %d", &A, &B);
    diff[A - 1]--;
    diff[B]++;
  }
  value[0] = M;
  sum[0] = 0;
  for (int i = 1; i < N + 1; i++) {
    value[i] = value[i - 1] + diff[i - 1];
    sum[i] = sum[i - 1] + value[i];
  }
  int min = 9999999;
  int l = 0;
  for (int r = 1; r <= N; r++) {
      while (l <= r && sum[r] - sum[l] >= K) {
         if (min > r - l) min = r - l;
         l++;
      }
  }
  printf("%d\n", min > N ? -1 : min);
  return 0;
}
