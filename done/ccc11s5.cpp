#include <cstdio>
#include <queue>
#include <map>

int n, a;
std::queue<int> q;
std::map<int, int> m;

inline int bitset(const int n, const int d) {
    return (n >> d) & 1;
}

inline void setbit(int& n, const int d) {
    n ^= (1 << d); 
}

int main() {
    scanf("%d", &n);
    for (int i = 0, input; i < n; i++) {
        scanf("%d", &input);
        a = 2 * a + input;
    }
        
    q.push(a);
    m[a] = 0;
    while (!q.empty()) {
        const int node = q.front(); q.pop();
        for (int i = 0; i < n; i++) {
            int next = node;
            if (!bitset(next, i)) {
                // printf("Turn on light #%d in %d\n", i, next);
                setbit(next, i);
                // Try turning it on and seeing what happens
                int count = 0;
                for (int j = 1; i + j < n && bitset(next, i + j); j++) {
                    count++;
                }
                for (int j = 1; i - j >= 0 && bitset(next, i - j); j++) {
                    count++;
                }
                if (count >= 3) {
                    // printf("Count is %d\n", count);
                    // printf("Number is %d\n", next);
                    setbit(next, i);
                    for (int j = 1; i + j < n && bitset(next, i + j); j++) {
                        setbit(next, i + j);
                    }
                    for (int j = 1; i - j >= 0 && bitset(next, i - j); j++) {
                        setbit(next, i - j);
                    }
                    // printf("Number is now %d\n", next);
                }
                if (next == 0) {
                    printf("%d\n", m[node] + 1);
                    return 0;
                }
                if (m.count(next) == 0) {
                    q.push(next);
                    m[next] = m[node] + 1;
                }
            }
        }
    }
    return 1;
}