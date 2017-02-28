#include "inaho.h"

#include <cstdio>
#include <vector>
#include <tuple>

int n, r[500005], s[500005], rank[500005];
std::vector<std::pair<int, int> > p;

int find(const int node) {
    if (r[node] == node) return node;
    return find(r[node]);
}

void Init(const int n) {
    for (int i = 1; i <= n; i++) { r[i] = i; s[i] = rank[i] = 1; }
}

void AddEdge(const int u, const int v) {
    const int ur = find(u), vr = find(v);
    int a = -1, b = -1;
    if (ur != vr) {
        if (rank[ur] > rank[vr]) {
            r[vr] = ur;
            s[ur] += s[vr];
            a = ur, b = vr;
        } else {
            r[ur] = vr;
            s[vr] += s[ur];
            if (rank[ur] == rank[vr])
                rank[vr]++;
            a = vr, b = ur;
        }
    }
    p.push_back(std::make_pair(a, b));
}

void RemoveLastEdge() {
    int u, v;
    std::tie(u, v) = p.back(); p.pop_back();
    if (u != -1) {
        r[v] = v;
        s[u] -= s[v];
    }
}

int GetSize(const int u) {
    return s[find(u)];
}