#include <stdio.h>
#include <stdlib.h>

#define min(a, b) ((a) < (b) ? (a) : (b))
#define p1 (2 * i + 1)
#define p2 (2 * i + 2)

typedef struct {
    int l, r, gcd, min, num_gcd;
} node;

static inline int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

int n, m, a, b;
char c;
node s[300001];

static inline void push_up(const int i) {
    s[i].gcd = gcd(s[p1].gcd, s[p2].gcd);
    s[i].min = min(s[p1].min, s[p2].min);
    s[i].num_gcd = 0;
    if (s[i].gcd == s[p1].gcd) s[i].num_gcd += s[p1].num_gcd;
    if (s[i].gcd == s[p2].gcd) s[i].num_gcd += s[p2].num_gcd;
}

static inline void change(const int i, const int index, const int value) {
    if (s[index].l == s[index].r && s[index].l == i) {
        s[index].min = s[index].gcd = value;
        s[index].num_gcd = 1;
        return;
    }
    const int mid = (s[index].l + s[index].r) / 2;
    if (s[index].l <= i && i <= mid) change(i, 2 * index + 1, value);
    else change(i, 2 * index + 2, value);
    push_up(index);
}

static inline int query_min(const int range_l, const int range_r, const int i) {
    if (range_l > s[i].r || range_r < s[i].l) return 0x3f3f3f3f;
    if (s[i].l >= range_l && s[i].r <= range_r) return s[i].min;
    return min(query_min(range_l, range_r, p1), query_min(range_l, range_r, p2));
}

static inline int query_gcd(const int range_l, const int range_r, const int i) {
    if (range_l > s[i].r || range_r < s[i].l) return 0;
    if (s[i].l >= range_l && s[i].r <= range_r) return s[i].gcd;
    return gcd(query_gcd(range_l, range_r, p1), query_gcd(range_l, range_r, p2));
}

static inline int query_num(const int range_l, const int range_r, const int i) {
    if (range_l > s[i].r || range_r < s[i].l) return 0;
    if (s[i].l >= range_l && s[i].r <= range_r) return s[i].num_gcd;
    const int first_half = query_gcd(range_l, range_r, p1);
    const int second_half = query_gcd(range_l, range_r, p2);
    const int total_gcd = gcd(first_half, second_half);
    int count = 0;
    if (total_gcd == first_half) count += query_num(range_l, range_r, p1);
    if (total_gcd == second_half) count += query_num(range_l, range_r, p2);
    return count;
}

static void init(const int l, const int r, const int i) {
    s[i].l = l; s[i].r = r;
    if (l == r) { scanf("%d", &a); s[i].gcd = s[i].min = a; s[i].num_gcd = 1; return; }
    const int mid = (l + r) / 2;
    init(l, mid, p1); init(mid + 1, r, p2);
    push_up(i);
}

int main() {
    scanf("%d %d", &n, &m);
    init(1, n, 0);
    getchar();

    while (m--) {
        c = getchar();
        scanf("%d %d", &a, &b);
        getchar();
        if (c == 'C') change(a, 0, b);
        else if (c == 'M') printf("%d\n", query_min(a, b, 0));
        else if (c == 'G') printf("%d\n", query_gcd(a, b, 0));
        else if (c == 'Q') printf("%d\n", query_num(a, b, 0));
    }
}