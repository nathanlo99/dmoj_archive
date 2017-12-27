#include <cstdio>

int months[12] = {4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2};

char* names[7] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
int d, m;

int main() {
    scanf("%d %d", &d, &m);
    printf("%s\n", names[(months[m - 1] + d - 1) % 7]);
}