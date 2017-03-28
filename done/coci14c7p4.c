#include <stdio.h>

int n, k;
long long ans;
static const long long a[8][3] = {
/*1*/   { 0, 2, 1572858 },
/*2*/   { 0, 0, 96 },
/*3*/   { 0, 2, 18 },
/*4*/   { 0, 2, 24570 },
/*5*/   { 0, 0, 12 },
/*6*/   { 0, 0, 6 },
/*7*/   { 0, 0, 96 },
/*8*/   { 0, 2, 1073741820 }
};

int main() {
    scanf("%d %d", &n, &k);
    ans = (long long)(k) * (k - 1) * (k - 2) / 6 * a[n - 1][2];
    ans += (long long)(k) * (k - 1) / 2 * a[n - 1][1];
    ans += (long long)(k) * a[n - 1][0];
    printf("%lld\n", ans);
}