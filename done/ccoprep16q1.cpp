#include <cstdio>
#include <stack>

int histogram[1001], k, m, n, ans, t;
int tp, i;

char c;
std::stack<int> s;

void get_max(int n) {
    i = 0;
    while (i < n) {
        if (s.empty() || histogram[s.top()] <= histogram[i]) {
            s.push(i++);
        } else {
            tp = s.top(); s.pop();
            if (s.empty()) ans = std::max(ans, histogram[tp] * i);
            else ans = std::max(ans, histogram[tp] * (i - s.top() - 1));
        }
    }
 
    while (!s.empty()) {
        tp = s.top(); s.pop();
        ans = std::max(ans, histogram[tp] * (s.empty() ? i : i - s.top() - 1));
    }
}

int main() {
    scanf("%d", &k);
    while (k--) {
        ans = 0;
        scanf(" %d %d", &m, &n);
        for (int i = 0; i < 1001; i++) histogram[i] = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                scanf(" %c", &c);
                if (c == 'R') histogram[j] = 0;
                else histogram[j]++;
            }
            get_max(n);
        }
        printf("%d\n", ans * 3);
    }
}