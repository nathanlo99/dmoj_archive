#include <stdio.h>

int r, s, fall_dist = 10000, last_meteor[3001], seen_meteor[3001];
char c, grid[3001][3001];

int main() {
    scanf("%d %d", &r, &s);
    for (int row = 0; row < r; row++) {
        scanf(" %s ", grid[row]);
        for (int col = 0; col < s; col++) {
            c = grid[row][col];
            if (c == 'X') {
                last_meteor[col] = row;
                seen_meteor[col] = 1;
            } else if (c == '#') {
                if (seen_meteor[col]) {
                    int dist = row - last_meteor[col] - 1;
                    if (dist < fall_dist)
                        fall_dist = dist;
                }
            }
        }
    }

    for (int row = 0; row < r; row++) {
        for (int col = 0; col < s; col++) {
            if (grid[row][col] == '#') {
                putchar('#');
            } else if (row >= fall_dist && grid[row - fall_dist][col] == 'X') {
                putchar('X');
            } else {
                putchar('.');
            }
        }
        putchar('\n');
    }

    return 0;
}