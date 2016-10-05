#include <stdio.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

long long n, m, lookup[(1 << 20) + 1], heap[(1 << 21) + 1], a, b, idx;
char c;

int main() {
    scanf("%lld %lld", &n, &m);
    // Get input
    for (int i = 1; i <= (1 << n); i++) {
        scanf("%lld", &lookup[i]);
        heap[(1 << n) + i - 1] = i;
    }
    
    for (int i = (1 << n) - 1; i >= 1; i--) {
        const register int a = heap[2 * i], b = heap[2 * i + 1];
        if (lookup[a] > lookup[b]) {
            heap[i] = a;
        } else {
            heap[i] = b;
        }
    }

    for (int i = 0; i < m; i++) {
        do { c = getchar(); } while (!(c == 'R' || c == 'W' || c == 'S'));
        switch(c) {
            case 'R':
                scanf("%lld %lld", &a, &b);
                idx = (1 << n) + a - 1;
                lookup[a] = b;
                idx >>= 1;
                while (idx >= 1) {
                    const register int v1 = heap[2 * idx];
                    const register int v2 = heap[2 * idx + 1];
                    if (lookup[v1] > lookup[v2]) {
                        heap[idx] = v1;
                    } else {
                        heap[idx] = v2;
                    }
                    idx >>= 1;
                }
                break;
            case 'W':
                printf("%lld\n", heap[1]);
                break;
            case 'S':
                scanf("%lld", &a);
                idx = (1 << n) + a - 1;
                const register int amount = heap[idx];
                b = 0;
                while (idx >= 1 && heap[idx] == amount) {
                    idx >>= 1;
                    b++;
                }
                printf("%lld\n", b - 1);
                break;
        }
    }
}