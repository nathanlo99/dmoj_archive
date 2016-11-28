#include <stdio.h>

#define getchar() (*_pbuf ? *_pbuf++ : (_buf[fread_unlocked(_pbuf = _buf, 1, 16384, stdin)] = 0, *_pbuf++))
char _buf[16385], *_pbuf = _buf;

int read() {
	int c, o = 0;
	while ((c = getchar()) < '0');
	do o = (o << 3) + (o << 1) + c - '0';
	while ((c = getchar()) >= '0');
	return o;
}

int n, m, a, b, root[100001], edges[100001], num_edges;

int find_root(int n) {
    return n == root[n] ? root[n] : (root[n] = find_root(root[n]));
}

int main() {
    n = read(); m = read();
    for (int i = 1; i <= n; i++) root[i] = i;

    for (int i = 1; i <= m; i++) {
        if (num_edges + 1 > n) break;
        a = read(); b = read();
        const int ar = find_root(a), br = find_root(b);
        if (ar != br) root[ar] = br, edges[num_edges++] = i;
    }
    
    if (num_edges + 1 < n) printf("Disconnected Graph\n");
    else for (int i = 0; i < num_edges; i++) printf("%d\n", edges[i]);
}