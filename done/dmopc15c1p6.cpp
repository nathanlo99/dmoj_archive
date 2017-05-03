#include <cstdio>

typedef struct {
    int l, r, value, lazy;
} node;

int m, n, q;
node seg[600000];

void pushup(int idx) {
    seg[idx].value = seg[2 * idx].value + seg[2 * idx + 1].value;
}

void pushdown(int idx) {
    seg[idx].value += seg[idx].lazy * (seg[idx].r - seg[idx].l + 1);
    seg[idx].value %= m;
    if (seg[idx].l != seg[idx].r) {
        seg[2 * idx].lazy += seg[idx].lazy;
        seg[2 * idx + 1].lazy += seg[idx].lazy;
        seg[2 * idx].lazy %= m;
        seg[2 * idx + 1].lazy %= m;
    }
    seg[idx].lazy = 0;
}

void init(int l, int r, int idx) {
    seg[idx].l = l;
    seg[idx].r = r;
    if (l == r) {
        scanf("%d", &seg[idx].value);
        seg[idx].value %= m;
    } else {
        const int mid = (l + r) / 2;
        init(l, mid, 2 * idx);
        init(mid + 1, r, 2 * idx + 1);
        pushup(idx);
    }
}

void update(int l, int r, int x, int idx) {
    pushdown(idx);
    if (seg[idx].l >= l && seg[idx].r <= r) {
        seg[idx].lazy += x;
        seg[idx].lazy %= m;
        pushdown(idx);
        return;
    }
    if (seg[idx].r < l || seg[idx].l > r) {
        return;
    }
    update(l, r, x, 2 * idx);
    update(l, r, x, 2 * idx + 1);
    pushup(idx);
}

int query(int l, int r, int idx) {
    pushdown(idx);
    if (seg[idx].l >= l && seg[idx].r <= r) {
        return seg[idx].value % m;
    }
    if (seg[idx].r < l || seg[idx].l > r) return 0;
    return (query(l, r, 2 * idx) + query(l, r, 2 * idx + 1)) % m;
}

int main() {
    scanf("%d %d %d", &m, &n, &q);
    init(1, n, 1);
    for (int i = 0, op, l, r, x; i < q; i++) {
        scanf("%d", &op);
        if (op == 1) {
            scanf("%d %d %d", &l, &r, &x);
            update(l, r, x, 1);
        } else {
            scanf("%d %d", &l, &r);
            printf("%d\n", query(l, r, 1));
        }
    }
    
}