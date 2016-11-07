#include <stdio.h>

#define min(a, b) (a) < (b) ? (a) : (b)
#define max(a, b) (a) > (b) ? (a) : (b)

typedef struct {
    int l, r, min, lazy;
} node;

int n, q, c, r, a, b;
node seg[90000];

void pushdown(int rt) {
    if (seg[rt].l == seg[rt].r || seg[rt].lazy == 0) return;
    seg[2 * rt].lazy += seg[rt].lazy;
    seg[2 * rt].min = max(0, seg[2 * rt].min - seg[rt].lazy);
    seg[2 * rt + 1].lazy += seg[rt].lazy;
    seg[2 * rt + 1].min = max(0, seg[2 * rt + 1].min - seg[rt].lazy);
    seg[rt].lazy = 0;
}

void build(int l, int r, int rt) {
    seg[rt].l = l; seg[rt].r = r;
    if (l == r) {
        scanf("%d", &seg[rt].min);
    } else {
        const int mid = (l + r) / 2;
        build(l, mid, 2 * rt);
        build(mid + 1, r, 2 * rt + 1);
        seg[rt].min = min(seg[2 * rt].min, seg[2 * rt + 1].min);
    }
}

void update(int l, int r, int rt, int v) {
    if (seg[rt].l == l && seg[rt].r == r) {
        seg[rt].min = max(0, seg[rt].min - v);
        seg[rt].lazy += v;
        return;
    }
    pushdown(rt);
    const int mid = (seg[rt].l + seg[rt].r) / 2;
    if (r <= mid) update(l, r, 2 * rt, v);
    else if (l > mid) update(l, r, 2 * rt + 1, v);
    else {
        update(l, mid, 2 * rt, v); update(mid + 1, r, 2 * rt + 1, v);
    }
    seg[rt].min = min(seg[2 * rt].min, seg[2 * rt + 1].min);
}

int query(int l, int r, int rt) {
    if (seg[rt].l == l && seg[rt].r == r) return seg[rt].min;
    pushdown(rt);
    const int mid = (seg[rt].l + seg[rt].r) / 2;
    if (r <= mid) return query(l, r, 2 * rt);
    else if (l > mid) return query(l, r, 2 * rt + 1);
    else {
        return min(query(l, mid, 2 * rt), query(mid + 1, r, 2 * rt + 1));
    }
}

int main() {
    scanf("%d %d", &n, &q);
    build(1, n, 1);
    while (q--) {
        scanf("%d %d %d", &a, &b, &c);
        update(a, b, 1, c);
        printf("%d %d\n", query(a, b, 1), seg[1].min);
    }
}