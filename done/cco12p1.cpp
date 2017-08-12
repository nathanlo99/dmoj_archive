#include <cstdio>
#include <set>

using namespace std;

set<int> dig;
int w, d, v, a, target;

int main() {
	scanf("%d %d", &w, &d);
	for (int i = 0; i < d; i++) {
		scanf("%d", &a);
		dig.insert(a);
	}
	scanf("%d", &v);
	for (int i = 0; i < v; i++) {
		scanf("%d", &target);
		set<int> things, last;
		for (int d: dig) last.insert(d);
		for (int i = 0; i < w; i++) {
			for (int d: dig) {
				for (int e: last) {
					things.insert(d + e);
					things.insert(d * e);
				}
			}
			last = things;
			things = set<int>();
		}
		printf("%c\n", "NY"[!!last.count(target)]);
	}
}