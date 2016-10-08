#include <cstdio>
#include <queue>
#include <tuple>
#include <utility>

typedef std::tuple<int, int, int> node_t;
int l, d, tx, ty, grid[1000][1000], dist[1000][1000], vis[1000][1000];
std::priority_queue<node_t> q;

int main() {
    scanf("%d %d", &l, &d);
    for (int i = 0; i < d; i++) for (int j = 0; j < l; j++) {
        scanf("%d", &grid[i][j]), dist[i][j] = 0x3f3f3f3f;
        q.push(std::make_tuple(-dist[i][j], j, i));
    }
    dist[0][0] = grid[0][0];
    q.push(std::make_tuple(-dist[0][0], 0, 0));

    scanf("%d %d", &tx, &ty);
    
    while (!q.empty()) {
        int cur_x, cur_y, cur_dist;
        std::tie(cur_dist, cur_x, cur_y) = q.top(); q.pop();
        cur_dist *= -1;
        if (vis[cur_y][cur_x]) continue;
        if (cur_x == tx && cur_y == ty) break;

        vis[cur_y][cur_x] = 1;
        
        if (cur_x > 0 && !vis[cur_y][cur_x - 1]) {
            int alt = cur_dist + grid[cur_y][cur_x - 1];
            if (alt < dist[cur_y][cur_x - 1]) {
                dist[cur_y][cur_x - 1] = alt;
                q.push(std::make_tuple(-alt, cur_x - 1, cur_y));
            }
        }

        if (cur_x < l && !vis[cur_y][cur_x + 1]) {
            int alt = cur_dist + grid[cur_y][cur_x + 1];
            if (alt < dist[cur_y][cur_x + 1]) {
                dist[cur_y][cur_x + 1] = alt;
                q.push(std::make_tuple(-alt, cur_x + 1, cur_y));
            }
        }

        if (cur_y < d && !vis[cur_y + 1][cur_x]) {
            int alt = cur_dist + grid[cur_y + 1][cur_x];
            if (alt < dist[cur_y + 1][cur_x]) {
                dist[cur_y + 1][cur_x] = alt;
                q.push(std::make_tuple(-alt, cur_x, cur_y + 1));
            }
        }
    }

    printf("%d\n", dist[ty][tx]);
}