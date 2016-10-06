#include <queue>
#include <cstdio>

typedef struct {
    int x, y, z;
} xyz;

int maxx, maxy, maxz, n, x, y, z, d, dist[101][101][101];
std::queue< xyz > q;

int main() {
    scanf("%d %d %d %d", &maxx, &maxy, &maxz, &n);
    for (int x = 1; x <= maxx; x++) {
        for (int y = 1; y <= maxy; y++) {
            for (int z = 1; z <= maxz; z++) {
                dist[x][y][z] = 0x3f3f3f3f;
            }
        }
    }
    dist[1][1][1] = 0;
    while (n--) {
        scanf("%d %d %d", &x, &y, &z);
        dist[x][y][z] = -1;
    }
    q.push((xyz){1, 1, 1});
    
    while (!q.empty()) {
        xyz cur = q.front(); q.pop();
        x = cur.x, y = cur.y, z = cur.z;
        d = dist[x][y][z];
        if (y == maxy && maxx - 2 <= x && x <= maxx && maxz - 2 <= z && z <= maxz) {
            printf("%d\n", d);
            break;
        }
        if (x > 2 && dist[x - 1][y][z] == 0x3f3f3f3f) {
            dist[x - 1][y][z] = d + 1;
            q.push((xyz){ x - 1, y, z });
        }
        if (x + 1 <= maxx && dist[x + 1][y][z] == 0x3f3f3f3f) {
            dist[x + 1][y][z] = d + 1;
            q.push((xyz){ x + 1, y, z });
        }
        if (y > 2 && dist[x][y - 1][z] == 0x3f3f3f3f) {
            dist[x][y - 1][z] = d + 1;
            q.push((xyz){ x, y - 1, z });
        }
        if (y + 1 <= maxy && dist[x][y + 1][z] == 0x3f3f3f3f) {
            dist[x][y + 1][z] = d + 1;
            q.push((xyz){ x, y + 1, z });
        }
        if (z > 2 && dist[x][y][z - 1] == 0x3f3f3f3f) {
            dist[x][y][z - 1] = d + 1;
            q.push((xyz){ x, y, z - 1 });
        }
        if (z + 1 <= maxz && dist[x][y][z + 1] == 0x3f3f3f3f) {
            dist[x][y][z + 1] = d + 1;
            q.push((xyz){ x, y, z + 1 });
        }
    }
    return 0;
}