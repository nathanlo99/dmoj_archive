#include <cstdio>
#include <string>
#include <iostream>

int ans;
std::string grid[16];
int main() {
    for (int i = 0; i < 7; i++) {
        std::getline(std::cin, grid[i + 2]);
        grid[i + 2] = "  " + grid[i + 2] + "  ";
    }
    grid[0] = grid[1] = grid[9] = grid[10] = "          ";
    for (int i = 2; i < 9; i++) {
        for (int j = 2; j < 9; j++) {
            if (grid[i][j] != '.') continue;
            if (grid[i - 1][j] == 'o' && grid[i - 2][j] == 'o') ans++;
            if (grid[i + 1][j] == 'o' && grid[i + 2][j] == 'o') ans++;
            if (grid[i][j - 1] == 'o' && grid[i][j - 2] == 'o') ans++;
            if (grid[i][j + 1] == 'o' && grid[i][j + 2] == 'o') ans++;
        }
    }
    printf("%d\n", ans);
}