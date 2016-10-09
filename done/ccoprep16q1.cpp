#include <cstdio>
#include <stack>
#include <cstring>
#include <string>
#include <iostream>

int histogram[1001], k, m, n, ans, t;
std::string buffer;
char c;

int get_max(int n) {
    std::stack<int> s;
    int max_area = 0, tp, i = 0;
    while (i < n) {
        if (s.empty() || histogram[s.top()] <= histogram[i]) {
            s.push(i++);
        } else {
            tp = s.top(); s.pop();
            if (s.empty()) max_area = std::max(max_area, histogram[tp] * i);
            else max_area = std::max(max_area, histogram[tp] * (i - s.top() - 1));
        }
    }
 
    while (!s.empty()) {
        tp = s.top(); s.pop();
        max_area = std::max(max_area, histogram[tp] * (s.empty() ? i : i - s.top() - 1));
    }
 
    return max_area;
}

int main() {
    std::cin >> k;
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
            ans = std::max(get_max(n), ans);
        }
        std::cout << ans * 3 << std::endl;
    }
}