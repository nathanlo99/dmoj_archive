#include <cstdio>
#include <cstring>
#include <iostream>
#define sqr(x) x *x
#define solution notNathansButWilliams
using namespace std;

int N, S, M[15];
int dp[(1 << 12) + 5][20];
int tmp[20];

int main() {
  scanf("%d%d", &N, &S);
  for (int i = 0; i < N; i++) {
    scanf("%d", &M[i]);
    for (int j = 0; j <= S; j++) {
      dp[1 << i][j] = sqr((M[i] + j)) + j;
    }
  }
  for (int i = 1; i < (1 << N); i++) {
    int cnt = 0;
    for (int j = 0; j < N; j++) {
      if (i & (1 << j)) {
        cnt++;
      }
    }
    if (cnt % 2 == 0)
      continue;
    for (int j = 1; j < i; j++) {
      if (!(i & j)) {
        for (int k = 0; k < N; k++) {
          if (!((i | j) & (1 << k))) {
            int idx = i | j | (1 << k);
            memset(tmp, 0, sizeof(tmp));
            for (int a = 0; a <= S; a++) {
              for (int b = 0; b <= a; b++) {
                tmp[a] = max(tmp[a], dp[i][b] * dp[j][a - b]);
              }
            }
            for (int a = S; a >= 0; a--) {
              for (int b = 0; b <= a; b++) {
                dp[idx][a] =
                    max(dp[idx][a], min(tmp[b], sqr((M[k] + a - b))) + a - b);
              }
            }
          }
        }
      }
    }
  }
  printf("%d", dp[(1 << N) - 1][S]);
  return 0;
}
