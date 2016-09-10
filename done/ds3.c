#include <stdio.h>
#include <stdlib.h>

typedef struct { int l, r, gcd, min, num_gcd; } node;

inline int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
inline int min(int a, int b) { return a > b ? b : a; }

int n, m, a, b;
node segment_tree[100000 * 3];

void push_up(int i) {
  segment_tree[i].gcd =
      gcd(segment_tree[2 * i + 1].gcd, segment_tree[2 * i + 2].gcd);
  segment_tree[i].min =
      min(segment_tree[2 * i + 1].min, segment_tree[2 * i + 2].min);
  int gcd1 = segment_tree[2 * i + 1].gcd;
  int gcd2 = segment_tree[2 * i + 2].gcd;
  segment_tree[i].num_gcd = 0;
  if (segment_tree[i].gcd == gcd1) {
    segment_tree[i].num_gcd += segment_tree[2 * i + 1].num_gcd;
  }
  if (segment_tree[i].gcd == gcd2) {
    segment_tree[i].num_gcd += segment_tree[2 * i + 2].num_gcd;
  }
}

void change(int i, int index, int value) {
    int l = segment_tree[index].l;
    int r = segment_tree[index].r;
    if (l == r && l == i) {
        segment_tree[index].min = value;
        segment_tree[index].gcd = value;
        segment_tree[index].num_gcd = 1;
        return;
    }
    int mid = (l + r) / 2;
    if (l <= i && i <= mid) {
        change(i, 2 * index + 1, value);
    } else {
        change(i, 2 * index + 2, value);
    }
    push_up(index);
}

void C(int i, int value) {
    change(i, 0, value);
}

void print() {
    int i = 0, c = 0;
    for (;;i++){
        printf("#%d: %d -> %d: min: %d, gcd: %d, num: %d\n", i, segment_tree[i].l, segment_tree[i].r, segment_tree[i].min, segment_tree[i].gcd, segment_tree[i].num_gcd);
        if (segment_tree[i].l == segment_tree[i].r) c++;
        if (c == n) break;
    }
}

int query_min(int range_l, int range_r, int i) {
    // No overlap: return 0x3f3f3f3f
    // Total overlap: return segment_tree[i].min
    // Partial overlap: return min(first_half, second_half);
    int l = segment_tree[i].l;
    int r = segment_tree[i].r;
    if (range_l > r || range_r < l) {
        return 0x3f3f3f3f;
    }
    if (l >= range_l && r <= range_r) {
        return segment_tree[i].min;
    }
    int first_half = query_min(range_l, range_r, 2 * i + 1);
    int second_half = query_min(range_l, range_r, 2 * i + 2);
    return min(first_half, second_half);
}

int query_gcd(int range_l, int range_r, int i) {
    int l = segment_tree[i].l;
    int r = segment_tree[i].r;
    if (range_l > r || range_r < l) {
        return 0;
    }
    if (l >= range_l && r <= range_r) {
        return segment_tree[i].gcd;
    }
    int first_half = query_gcd(range_l, range_r, 2 * i + 1);
    int second_half = query_gcd(range_l, range_r, 2 * i + 2);
    return gcd(first_half, second_half);
}

int query_num(int range_l, int range_r, int i) {
    int l = segment_tree[i].l;
    int r = segment_tree[i].r;
    if (range_l > r || range_r < l) {
        return 0;
    }
    if (l >= range_l && r <= range_r) {
        return segment_tree[i].num_gcd;
    }
    int first_half = query_gcd(range_l, range_r, 2 * i + 1);
    int second_half = query_gcd(range_l, range_r, 2 * i + 2);
    int first_num = query_num(range_l, range_r, 2 * i + 1);
    int second_num = query_num(range_l, range_r, 2 * i + 2);
    int total_gcd = gcd(first_half, second_half);
    int count = 0;
    if (total_gcd == first_half) count += first_num;
    if (total_gcd == second_half) count += second_num;
    return count;
}

void init(int l, int r, int i) {
  segment_tree[i].l = l;
  segment_tree[i].r = r;
  if (l != r) {
    int mid = (l + r) / 2;
    init(l, mid, 2 * i + 1);
    init(mid + 1, r, 2 * i + 2);
    push_up(i);
  } else {
    scanf("%d", &a);
    segment_tree[i].gcd = a;
    segment_tree[i].min = a;
    segment_tree[i].num_gcd = 1;
  }
}

int main() {
  scanf("%d %d", &n, &m);
  init(1, n, 0);
  getchar();
  char command;

  for (int i = 0; i < m; i++) {
    command = getchar();
    scanf("%d %d", &a, &b);
    getchar();
    if (command == 'C') {
        C(a, b);
    } else if (command == 'M') {
        printf("%d\n", query_min(a, b, 0));
    } else if (command == 'G') {
        printf("%d\n", query_gcd(a, b, 0));
    } else if (command == 'Q') {
        printf("%d\n", query_num(a, b, 0));
    }
  }
  return 0;
}