#include <stdio.h>

int n, q, x1, y1, z1, x2, y2, z2, l;
long long height[256][256][256], bit[256][256][256], ans;
char opcode;

void update(int x, int y, int z, int v) {
    int xx = x;
    while (xx <= 256) {
        register int yy = y;
        while (yy <= 256) {
            register int zz = z;
            while (zz <= 256) {
                bit[xx][yy][zz] += v;
                zz += zz & -zz;
            }
            yy += yy & -yy;
        }
        xx += xx & -xx;
    }
}

long long query(int x, int y, int z) {
    register long long res = 0;
    register int xx = x;
    while (xx > 0) {
        register int yy = y;
        while (yy > 0) {
            register int zz = z;
            while (zz > 0) {
                res += bit[xx][yy][zz];
                zz -= zz & -zz;
            }
            yy -= yy & -yy;
        }
        xx -= xx & -xx;
    }
    return res;
}

long long query_bit(int x1, int y1, int z1, int x2, int y2, int z2) {
    return query(x2, y2, z2)
        - query(x1 - 1, y2, z2) - query(x2, y1 - 1, z2) - query(x2, y2, z1 - 1)
        + query(x1 - 1, y1 - 1, z2) + query(x1 - 1, y2, z1 - 1) + query(x2, y1 - 1, z1 - 1)
        - query(x1 - 1, y1 - 1, z1 - 1);
}

int main() {
    scanf("%d %d", &n, &q);
    while (q--) {
        scanf(" %c", &opcode);
        if (opcode == 'C') {
            scanf("%d %d %d %d", &x1, &y1, &z1, &l);
            update(x1, y1, z1, l - height[x1][y1][z1]);
            height[x1][y1][z1] = l;
        } else {
            scanf("%d %d %d %d %d %d", &x1, &y1, &z1, &x2, &y2, &z2);
            ans += query_bit(x1, y1, z1, x2, y2, z2);
        }
    }
    printf("%lld\n", ans);
}