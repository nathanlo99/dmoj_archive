#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n, a, q, x, y, day = 1;
char op;
vector<pair<int, int>> thing[1000005];

int query(int x, int y) {
	int i = upper_bound(thing[x].begin(), thing[x].end(), make_pair(y, 0x3f3f3f3f)) - thing[x].begin();
	return thing[x][i - 1].second;
}

int main() {
	scanf("%d ", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d ", &a);
		thing[i].push_back(make_pair(0, a));
	}
	scanf("%d ", &q);
	for (int i = 0; i < q; i++) {
		scanf("%c %d %d ", &op, &x, &y);
		if (op == 'C') {
		    thing[x].push_back(make_pair(day, y));
			day++;
		} else {
			/*
			for (int j = 1; j <= n; j++) {
				printf("%d: ", j);
				for (int d = 0; d <= day; d++) {
					printf("%d ", query(j, d));
				}
				printf("\n");
			}
			*/
			printf("%d\n", query(x, y));
		}
	}
}