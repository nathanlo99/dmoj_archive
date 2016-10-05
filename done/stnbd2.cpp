#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
using ll = long long;

ll n, m, s, e, ans;
vector<vector<ll>> g;
vector<ll> indeg, outdeg;
vector<pair<ll, ll>> nodes;
int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n >> m;
	g.resize(n + 1);
	nodes.resize(n + 1);
	indeg.resize(n + 1);
	outdeg.resize(n + 1);
	for (int i = 0; i < m; i++) {
		cin >> s >> e;
		g.at(s).push_back(e);
		indeg.at(e)++;
		outdeg.at(s)++;
	}
	for (int i = 1; i <= n; i++) {
		if (indeg.at(i) == 0) {
			nodes.at(i).second = 1;
			nodes.at(i).first = 0;
		}
	}
	for (int i = 1; i <= n; i++) {
		for (const auto &a : g.at(i)) {
			nodes.at(a).first = (nodes.at(a).first + nodes.at(i).first + nodes.at(i).second) % 1000000007;
			nodes.at(a).second = (nodes.at(a).second + nodes.at(i).second) % 1000000007;
		}
	}
	for (int i = 1; i <= n; i++) {
		if (outdeg.at(i) == 0) {
			ans = (ans + nodes.at(i).first) % 1000000007;
		}
	}

	cout << ans << endl;
}