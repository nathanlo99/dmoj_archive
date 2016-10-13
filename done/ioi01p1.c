#include <stdio.h>

unsigned int bit[1050][1050];

int opcode, s, t1, t2, t3, t4;

void update(int x, int y, int a) {
    for (int xx = x; xx <= s; xx += xx & -xx)
        for (int yy = y; yy <= s; yy += yy & -yy)
            bit[xx][yy] += a;
}

unsigned long long query(int x, int y) {
    x++; y++;
    unsigned long long ans = 0;
    for (int xx = x; xx > 0; xx -= xx & -xx) 
        for (int yy = y; yy > 0; yy -= yy & -yy)
            ans += bit[xx][yy];
    return ans;
}

int main() {
    scanf("%d %d", &opcode, &s);
    while (1) {
        scanf("%d", &opcode);
        if (opcode == 1) {
            scanf("%d %d %d", &t1, &t2, &t3);
            update(t1 + 1, t2 + 1, t3);
        } else if (opcode == 2) {
            scanf("%d %d %d %d", &t1, &t2, &t3, &t4);
            printf("%lld\n", query(t3, t4) - query(t1 - 1, t4) - query(t3, t2 - 1) + query(t1 - 1, t2 - 1));
        } else {
            break;
        }
    }
}