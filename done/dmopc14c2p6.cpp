/*
5
1 3 4 2 5
5
0 4 3
1 3 2
0 4 5
4 4 1
0 4 1
*/
#include <cstdio>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

int n, q, qn, a, b, c, s[100005], qa[100005], bit[100005];

vector<int> idx[20005];
vector<tuple<int, int, int>> events[20005];

void update(int a, int amt) {
	a++;
	for (; a <= 100005; a += a & -a) bit[a] += amt;
}

int query(int a) {
	a++;
	int res = 0;
	for (; a > 0; a -= a & -a) res += bit[a];
	return res;
}

int query(int a, int b) {
	return query(b) - query(a - 1);
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &s[i]);
		idx[s[i]].push_back(i);
	}
	scanf("%d", &q);
	for (int i = 0; i < q; i++) {
		scanf("%d %d %d", &a, &b, &c);
		events[c].push_back(make_tuple(a, b, i));
	}

	for (int i = 20005; i >= 0; i--) {
		for (int v : idx[i]) update(v, i);
		for (auto v : events[i]) {
			tie(a, b, qn) = v;
			qa[qn] = query(a, b);
		}
	}

	for (int i = 0; i < q; i++) {
		printf("%d\n", qa[i]);
	}
}