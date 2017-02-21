#include <cstdio>
#include <cstdlib>
#include <queue>
#include <tuple>
#include <cstring>

int t, l, w, cx, cy, nx, ny, sx, sy, tx, ty, dist[51][51], vis[51][51];
char grid[51][51];
std::queue <std::pair<int, int> > q;

int main() {
    scanf("%d", &t);
    for (int _ = 0; _ < t; _++) {
        scanf("%d %d", &l, &w);
        for (int i = 0; i < w; i++) {
            scanf("%s", grid[i]);
            for (int j = 0; j < l; j++) {
                if (grid[i][j] == 'C') {
                    sx = j;
                    sy = i;
                } else if (grid[i][j] == 'W') {
                    tx = j;
                    ty = i;
                } else if (grid[i][j] == 'O') {
                    grid[i][j] = '.';
                }
            }
        }
        
        while (!q.empty()) q.pop();
        memset(dist, 0, sizeof(dist)), memset(vis, 0, sizeof(vis));
        
        q.push(std::make_pair(sx, sy));
        dist[sy][sx] = 0;
        vis[sy][sx] = 1;
        
        while (!q.empty()) {
            std::tie(cx, cy) = q.front();
            q.pop();
            if (dist[cy][cx] == 61) break;
            for (auto xy: {std::make_pair(cx - 1, cy), std::make_pair(cx + 1, cy),
                           std::make_pair(cx, cy - 1), std::make_pair(cx, cy + 1)} ) {
                std::tie(nx, ny) = xy;
                if (nx >= 0 && nx < l && ny >= 0 && ny < w && 
                        grid[ny][nx] != 'X' && !vis[ny][nx]) {
                    dist[ny][nx] = dist[cy][cx] + 1;
                    vis[ny][nx] = 1;
                    q.push(std::make_pair(nx, ny));
                }
            }
        }
        
        if (vis[ty][tx] && dist[ty][tx] < 60) {
            printf("%d\n", dist[ty][tx]);
        } else {
            printf("#notworth\n");
        }
    }
}