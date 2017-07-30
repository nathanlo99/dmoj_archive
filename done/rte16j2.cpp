#include <string>
#include <queue>
#include <tuple>

using namespace std;

int n, num;
char c, s[10];
priority_queue<pair<int, int>> stack;

const char* names[] = {"BLUE", "PINK", "GREEN"};

int main() {
    scanf("%d ", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s ", s);
		if (*s == 'A') {
		    scanf("%s %d ", s, &num);
			if (*s == 'B') stack.push(make_pair(0, -num));
			else if (*s == 'P') stack.push(make_pair(-1, -num));
			else if (*s == 'G') stack.push(make_pair(-2, -num));
		} else if (*s == 'N') {
		    if (stack.empty()) printf("NONE\n");
		    else {
		        int c, a;
		        tie(c, a) = stack.top(); stack.pop();
		        printf("%s %d\n", names[-c], -a);
		    }
		} else {
			printf("BAD %c\n", c);
		}
	}
}