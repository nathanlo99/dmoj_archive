#include <cstdio>
#include <cmath>

int n;

int main() {
    for (int i = 0; i < 5; i++) {
        scanf("%d", &n);
        printf("%d\n", 1000 * (int)ceil(n / 693.0)); 
    }
}