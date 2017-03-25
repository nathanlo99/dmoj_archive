#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>

int n, m, a, b;
int t[100005][26];
std::vector<int> num[100005], words[100005];
int count = 1;
char c, s[100005];

#define cnt(arr, a, b) (std::upper_bound(arr.begin(), arr.end(), b) - std::lower_bound(arr.begin(), arr.end(), a))

int main() {
    scanf("%d %d ", &n, &m);
    for (int i = 0; i < n; i++) {
        int cur = 0;
        while ((c = getchar()) != '\n') {
            num[cur].push_back(i + 1);
            if (!t[cur][c - 'a']) t[cur][c - 'a'] = count++;
            cur = t[cur][c - 'a'];
        }
        words[cur].push_back(i + 1);
    }
    scanf("%d", &m);
    while (m--) {
        scanf("%s %d %d", s, &a, &b);
        const int len = strlen(s);
        int cur = 0, ans = 0;
        for (int i = 0; i < len; i++) {
            if (!t[cur][s[i] - 'a']) break;
            else cur = t[cur][s[i] - 'a'];
            if (words[cur].size() != 0) ans += cnt(words[cur], a, b);
            if (i == len - 1) ans += cnt(num[cur], a, b);
        }
        printf("%d\n", ans);
    }
}