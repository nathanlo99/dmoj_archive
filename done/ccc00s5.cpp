#include <cstdio>
#include <vector>

int n, danger[105];
double x[105], y[105];
std::vector<int> in_danger;

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lf %lf", &x[i], &y[i]);
    }
    for (double xx = 0.0; xx <= 1000.0; xx += 0.05) {
        double min_sqr_dist = 2e7;
        in_danger.clear();
        for (int i = 0; i < n; i++) {
            double sqr_dist = (xx - x[i]) * (xx - x[i]) + y[i] * y[i];
            if (sqr_dist < min_sqr_dist) {
                in_danger.clear();
                in_danger.push_back(i);
                min_sqr_dist = sqr_dist;
            } else if (sqr_dist == min_sqr_dist) {
                in_danger.push_back(i);
            }
        }
        for (int i : in_danger) {
            // if (!danger[i]) printf("%.2f, %.2f is in danger if being eaten at %.2f\n", x[i], y[i], xx);
            danger[i] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        if (danger[i]) {
            printf("The sheep at (%.2f, %.2f) might be eaten.\n", x[i], y[i]);
        }
    }
}