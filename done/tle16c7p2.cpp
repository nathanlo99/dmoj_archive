#include <cstdio>
#include <cmath>
#include <queue>

int n, t, x[100005], y[100005], tt, s;
double cx = 0.0, cy = 0.0, ans = 0.0;
int time_ = 0, team1 = 0;
std::queue<int> q;

int main() {
    scanf("%d %d", &n, &t);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x[i], &y[i]);
    }

    for (int i = 0; i < t; i++) {
        scanf("%d %d", &s, &tt);
        double remaining = tt - time_;
        while (remaining > 0) {
            int target = -1;
            if (team1) target = 0;
            else if (q.size() > 0) target = q.front();
            if (target == -1) break;
            double tx = x[target], ty = y[target];
            double dx = (tx - cx), dy = (ty - cy);
            double dist = sqrt(dx * dx + dy * dy);
            if (dist > remaining) {
                cx += dx * remaining / dist;
                cy += dy * remaining / dist;
                ans += remaining;
                remaining = 0;
            } else {
                remaining -= dist;
                cx = tx;
                cy = ty;
                ans += dist;
                if (target == 0) team1 = 0;
                else q.pop();
            }
        }
        if (s == 1) team1 = 1;
        else q.push(s - 1);
        time_ = tt;
    }
    while (true) {
        int target = -1;
        if (team1) target = 0;
        else if (q.size() > 0) target = q.front();
        if (target == -1) break;
        double tx = x[target], ty = y[target];
        double dist = sqrt((cx - tx) * (cx - tx) + (cy - ty) * (cy - ty));
        ans += dist;
        cx = tx;
        cy = ty;
        if (target == 0) team1 = 0;
        else q.pop();
    }
    printf("%lf\n", ans);
}