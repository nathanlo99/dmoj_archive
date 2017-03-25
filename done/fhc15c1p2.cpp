#include <cstdio>
#include <cstring>

int trie[1000005][26], num[1000005], t, n, ans, count;
char s[1000005];

int main() {
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        memset(trie, 0, sizeof(trie));
        memset(num, 0, sizeof(num));
        count = 1;
        ans = 0;
        scanf("%d ", &n);
        for (int a = 0; a < n; a++) {
            scanf("%s\n", s);
            const int l = strlen(s);
            int cur = 0;
            for (int i = 0; i < l; i++) {
                if (!trie[cur][s[i] - 'a']) trie[cur][s[i] - 'a'] = count++;
                cur = trie[cur][s[i] - 'a'];
                num[cur]++;
            }
            cur = 0;
            for (int i = 0; i < l; i++) {
                ans++;
                cur = trie[cur][s[i] - 'a'];
                if (num[cur] == 1) break;
            }
        }
        printf("Case #%d: %d\n", i, ans);
    }
}