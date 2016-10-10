#include <cstdio>
#include <queue>
#include <tuple>

int maxx, maxy, maxz, sx, sy, sz, x, y, z, cur_dist, ans;
int grid[155][155][155], vis[155][155][155], dist[155][155][155];
std::priority_queue<std::tuple<int, int, int, int> > q;
char c;

int main() {
    // Input
    scanf("%d %d %d", &maxx, &maxy, &maxz);
    for (int z = 1; z <= maxz; z++) {
        for (int y = 1; y <= maxy; y++) {
            for (int x = 1; x <= maxx; x++) {
                scanf(" %c", &c);
                if (c == 'J') {
                    dist[x][y][z] = 0;
                    grid[x][y][z] = 0;
                    q.push(std::make_tuple(0, x, y, z));
                    sx = x; sy = y; sz = z;
                } else {
                    grid[x][y][z] = c - '0';
                    dist[x][y][z] = 0x3f3f3f3f;
                    q.push(std::make_tuple(-dist[x][y][z], x, y, z));
                }
            }
        }
    }

    while (!q.empty()) {
        std::tie(cur_dist, x, y, z) = q.top(); q.pop();
        cur_dist *= -1;
        if (x == 1 || y == 1 || z == 1 || x == maxx || y == maxy || z == maxz) {
            printf("%d\n", cur_dist);
            break;
        }
        vis[x][y][z] = 1;
        
        // X
        if (!vis[x - 1][y][z]) {
            int alt = cur_dist + grid[x - 1][y][z];
            if (alt < dist[x - 1][y][z]) {
                dist[x - 1][y][z] = alt;
                q.push(std::make_tuple(-alt, x - 1, y, z));
            }
        }
        if (!vis[x + 1][y][z]) {
            int alt = cur_dist + grid[x + 1][y][z];
            if (alt < dist[x + 1][y][z]) {
                dist[x + 1][y][z] = alt;
                q.push(std::make_tuple(-alt, x + 1, y, z));
            }
        }
        
        // Y
        if (!vis[x][y - 1][z]) {
            int alt = cur_dist + grid[x][y - 1][z];
            if (alt < dist[x][y - 1][z]) {
                dist[x][y - 1][z] = alt;
                q.push(std::make_tuple(-alt, x, y - 1, z));
            }
        }
        if (!vis[x][y + 1][z]) {
            int alt = cur_dist + grid[x][y + 1][z];
            if (alt < dist[x][y + 1][z]) {
                dist[x][y + 1][z] = alt;
                q.push(std::make_tuple(-alt, x, y + 1, z));
            }
        }

        // Z
        if (!vis[x][y][z - 1]) {
            int alt = cur_dist + grid[x][y][z - 1];
            if (alt < dist[x][y][z - 1]) {
                dist[x][y][z - 1] = alt;
                q.push(std::make_tuple(-alt, x, y, z - 1));
            }
        }
        if (!vis[x][y][z + 1]) {
            int alt = cur_dist + grid[x][y][z + 1];
            if (alt < dist[x][y][z + 1]) {
                dist[x][y][z + 1] = alt;
                q.push(std::make_tuple(-alt, x, y, z + 1));
            }
        }

    }
    

}