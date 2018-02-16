#include <stdio.h>

int n;
int grid[101][101];

void rotate() {
    int temp[101][101];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            temp[i][j] = grid[j][n - i - 1];
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < n; j++)
            grid[i][j] = temp[i][j];
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < n; j++) 
            scanf("%d ", &grid[i][j]);
    while (grid[1][0] <= grid[0][0] || grid[0][1] <= grid[0][0]) rotate();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
}