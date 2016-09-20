#include <stdio.h>

int n, m, a, b, root[100001], edges[100001], num_edges;

int find_root(int n) {
    return n == root[n] ? root[n] : (root[n] = find_root(root[n]));
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) {
        root[i] = i;
    }

    for (int i = 1; i <= m; i++) {
        if (num_edges + 1 > n) {
            break;
        }   
        scanf("%d %d", &a, &b);
        int ar = find_root(a), br = find_root(b);
        if (ar != br) {
            root[ar] = br;
            edges[num_edges++] = i;
        }
    }
    
    if (num_edges + 1 < n) {
        printf("Disconnected Graph\n");
    } else {
        for (int i = 0; i < num_edges; i++) {
            printf("%d\n", edges[i]);
        }
    }

    return 0;
}