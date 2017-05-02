#include <cstdio>
#include <set>

using namespace std;

int n, m;
char grid[101][101];
int room_num[101][101];
int rooms[4];
int max_num, x, y;
set<int> temp, ans;

void dfs(int i, int j, int room) {
    if (grid[i][j] != '.') return;
    room_num[i][j] = room;
    grid[i][j] = 'O';
    dfs(i + 1, j, room);
    dfs(i - 1, j, room);
    dfs(i, j + 1, room);
    dfs(i, j - 1, room);
}

int main() {
    scanf("%d%d ", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            grid[i][j] = getchar();
        }
        getchar();
    }

    int room = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '.') dfs(i, j, room++);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] != 'X') continue;
            int a = room_num[i - 1][j],
                b = room_num[i + 1][j],
                c = room_num[i][j - 1],
                d = room_num[i][j + 1];
            temp.clear();
            if (a > 0) temp.insert(a);
            if (b > 0) temp.insert(b);
            if (c > 0) temp.insert(c);
            if (d > 0) temp.insert(d);
            if (temp.size() > max_num) {
                x = j; y = i;
                max_num = temp.size();
                ans = temp;
            }
        }
    }

    printf("%d\n%d %d\n", max_num, x, y);
    for (int a : ans) printf("%d ", a);
    printf("\n");
    
}