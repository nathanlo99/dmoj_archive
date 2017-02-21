#include <cstdio>
#include <vector>
#include <deque>

int a, b, c, w, s[3], sum[3];
std::deque<int> q[3];

#define max(a, b) ((a) > (b) ? (a) : (b))
#define max_sum (max(max(sum[0], sum[1]), sum[2]))

inline int max_length() {
    int a = q[0].size(), b = q[1].size(), c = q[2].size();
    if (a > b && a > c) return 0;
    if (b > a && b > c) return 1;
    if (c > a && c > b) return 2;
    return -1;
}

inline int min_length() {
    int a = q[0].size(), b = q[1].size(), c = q[2].size();
    if (a < b && a < c) return 0;
    if (b < a && b < c) return 1;
    if (c < a && c < b) return 2;
    return -1;
}

int main() {
    scanf("%d %d %d", &s[0], &s[1], &s[2]);
    for (int n = 0; n < 3; n++) {
        for (int i = 0; i < s[n]; i++) {
            scanf("%d", &w);
            q[n].push_back(w);
            sum[n] += w;
        }
    }
    int ans = 0;
    while (true) {
        /* for (int i = 0; i < 3; i++) {
            printf("%d: ", sum[i]);
            for (int j = 0; j < q[i].size(); j++) {
                printf("%d ", q[i][j]);
            }
            printf("\n");
        } */
        if (max_sum <= 30) {
            ans += max_sum;
            break;
        } else {
            ans += 30;
            // Shave off 30 and move people
            for (int i = 0; i < 3; i++) {
                int t = 30;
                while (!q[i].empty() && t > q[i][0]) {
                    t -= q[i][0];
                    sum[i] -= q[i][0];
                    q[i].pop_front();
                }
                if (!q[i].empty()) {
                    q[i][0] -= t;
                    sum[i] -= t;
                    if (q[i][0] == 0) q[i].pop_front();
                }
            }
            int longest = max_length();
            int shortest = min_length();
            if (longest != -1 && shortest != -1) {
                int last = q[longest][q[longest].size() - 1];
                q[longest].pop_back();
                sum[longest] -= last;
                q[shortest].push_back(last);
                sum[shortest] += last;
            }
        }
    }
    printf("%d\n", ans);
}