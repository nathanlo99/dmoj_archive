#include <cstdio>
#include <queue>
#include <map>

typedef unsigned long long stack_t;

int n, t, done;
std::queue<stack_t> q;
std::map<stack_t, int> dist;

int get_stack(stack_t stacks, int num) {
    return (stacks >> (8 * num)) & 255;
}

int top(stack_t stacks, int num) {
    int stack = (stacks >> (8 * num)) & 255;
    for (int i = 0; i < 8; i++) 
        if ((stack >> i) & 1) return i;
    return 8;
}

// Moves the top element of stack a onto stack b
stack_t move(stack_t stacks, int a, int b) {
    int a_top = top(stacks, a);
    stack_t mask = (1ULL << (8 * a + a_top)) | (1ULL << (8 * b + a_top));
    stack_t res = stacks ^ mask;
    return res;
}

int main() {
    for (;;) {
        scanf("%d", &n);
        if (!n) break;
        stack_t initial = 0;
        stack_t target = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &t);
            initial |= 1ULL << (8 * i + t);
            target |= 1ULL << (8 * (n - i - 1) + n - i);
        }
        dist.clear();
        while (!q.empty()) q.pop();
        q.push(initial);
        dist[initial] = 0;
        done = 0;
        while (!q.empty()) {
            stack_t cur = q.front(); q.pop();
            int d = dist[cur];
            if (cur == target) {
                printf("%d\n", d);
                done = 1;
                break;
            }
            for (int i = 0; i < n; i++) {
                int i_top = top(cur, i);
                if (i_top == 8) continue;
                if (i != 0 && i_top < top(cur, i - 1)) {
                    stack_t next = move(cur, i, i - 1);
                    if (dist.find(next) == dist.end()) {
                        dist[next] = d + 1;
                        q.push(next);
                    }
                }
                if (i != n - 1 && i_top < top(cur, i + 1)) {
                    stack_t next = move(cur, i, i + 1);
                    if (dist.find(next) == dist.end()) {
                        dist[next] = d + 1;
                        q.push(next);
                    }
                }
            }
        }
        if (!done) printf("IMPOSSIBLE\n");
    }
}