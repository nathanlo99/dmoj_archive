#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

int n;
std::string s;
std::vector<int> adj[26];
int vis[26];
int act[26];
int elem[26][26];

void dfs(int n, int last) {
	if (last != -1) {
		for (int i = 0; i < 26; i++) elem[n][i] |= elem[last][i];
	}
	if (!vis[n]) {
		vis[n] = 1;
		for (int next : adj[n]) dfs(next, n);
	}
}

int main() {
	scanf("%d ", &n);
	while (n--) {
		std::getline(std::cin, s);
		const char a = s[0], b = s[11];
		act[a - 'A'] = 1;
		memset(vis, 0, sizeof(vis));
		if ('A' <= b && b <= 'Z') {
			act[b - 'A'] = 1;
			adj[b - 'A'].push_back(a - 'A');
			dfs(b - 'A', -1);
		} else {
			elem[a - 'A'][b - 'a'] = 1;
			dfs(a - 'A', -1);
		}
	}
	for (int i = 0; i < 26; i++) {
		if (act[i]) {
			int flag = 0;
			printf("%c = {", 'A' + i);
			for (int j = 0; j < 26; j++) {
				if (elem[i][j]) {
					if (flag) printf(",");
					else flag = 1;
					printf("%c", j + 'a');
				}
			}
			printf("}\n");
		}
	}
}