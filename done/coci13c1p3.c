#include "stdio.h"

int n, ans = 0;
int a[101][101];

int sum[5000000];
int psa[101][101];

int get_sum(int x1, int y1, int x2, int y2) {
  if (x1) {
    if (y1) {
      return psa[x2][y2] - psa[x1 - 1][y2] - psa[x2][y1 - 1] +
             psa[x1 - 1][y1 - 1];
    } else {
      return psa[x2][y2] - psa[x1 - 1][y2];
    }
  } else {
    if (y1) {
      return psa[x2][y2] - psa[x2][y1 - 1];
    } else {
      return psa[x2][y2];
    }
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      scanf("%d", &a[i][j]);

  psa[0][0] = a[0][0];

  for (int i = 1; i < n; i++) {
    psa[i][0] = psa[i - 1][0] + a[i][0];
    psa[0][i] = psa[0][i - 1] + a[0][i];
  }

  for (int i = 1; i < n; i++)
    for (int j = 1; j < n; j++)
      psa[i][j] = psa[i][j - 1] + psa[i - 1][j] - psa[i - 1][j - 1] + a[i][j];

  int ans = 0;

  for (int pivot_x = 1; pivot_x < n; pivot_x++) {
    for (int pivot_y = 1; pivot_y < n; pivot_y++) {
      for (int x = 0; x < pivot_x; x++) {
        for (int y = 0; y < pivot_y; y++) {
          sum[get_sum(x, y, pivot_x - 1, pivot_y - 1) + 2500000]++;
        }
      }

      for (int x = pivot_x; x < n; x++) {
        for (int y = pivot_y; y < n; y++) {
          ans += sum[get_sum(pivot_x, pivot_y, x, y) + 2500000];
        }
      }

      for (int x = 0; x < pivot_x; x++) {
        for (int y = 0; y < pivot_y; y++) {
          sum[get_sum(x, y, pivot_x - 1, pivot_y - 1) + 2500000]--;
        }
      }
      for (int x = 0; x < pivot_x; x++) {
        for (int y = pivot_y; y < n; y++) {
          sum[get_sum(x, pivot_y, pivot_x - 1, y) + 2500000]++;
        }
      }
      for (int x = pivot_x; x < n; x++) {
        for (int y = 0; y < pivot_y; y++) {
          ans += sum[get_sum(pivot_x, y, x, pivot_y - 1) + 2500000];
        }
      }
      for (int x = 0; x < pivot_x; x++) {
        for (int y = pivot_y; y < n; y++) {
          sum[get_sum(x, pivot_y, pivot_x - 1, y) + 2500000]--;
        }
      }
    }
  }
  printf("%d\n", ans);
}