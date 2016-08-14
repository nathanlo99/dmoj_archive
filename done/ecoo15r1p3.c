#include "math.h"
#include "stdio.h"
#include "stdlib.h"

double x, y, s;
double px[11], py[11];

int n;

const static int first[5] = {1, 2, 4, 7, 11};

int main() {
  for (int i = 0; i < 10; i++) {
    double x1, y1, s1;
    int x2, y2, s2;
    scanf("%lf %d %lf %d %lf %d %d", &x1, &x2, &y1, &y2, &s1, &s2, &n);
    x = x1 * pow(10, x2);
    y = y1 * pow(10, y2);
    s = s1 * pow(10, s2);
    double dx = -s / 6;
    double dy = s * sqrt(3) / 6;
    double dxx = s / 3;
    for (int row = 0; row <= 3; row++) {
      double xx = x + dx * row;
      double yy = y + dy * row;
      for (int col = first[row]; col < first[row + 1]; col++) {
        px[col] = xx + dxx * (col - first[row]);
        py[col] = yy;
      }
    }
    for (int j = 0; j < 5; j++) {
      scanf("%lf %d %lf %d", &x1, &x2, &y1, &y2);
      x = x1 * pow(10, x2);
      y = y1 * pow(10, y2);
      double minDist = sqrt(pow(x - px[1], 2) + pow(y - py[1], 2));
      int minIndex = 1;
      for (int k = 2; k <= 10; k++) {
        double dist = sqrt(pow(x - px[k], 2) + pow(y - py[k], 2));
        if (dist < minDist) {
          minDist = dist;
          minIndex = k;
        }
      }
      printf("%d ", minIndex);
    }
    printf("\n");
  }
}
