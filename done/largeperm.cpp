#include <bits/stdc++.h>
using namespace std;

int a[100002], id[100002], n, k, temp;

int main() {
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
        id[a[i]] = i;
    }
    
    for (int i = 1; i <= n && k != 0; i++) {
        if (a[i] != n - i + 1) {
            k--;
            temp = a[i];
            swap(a[i], a[id[n - i + 1]]);
            swap(id[temp], id[n - i + 1]);
        }
    }
    
    for (int i = 1; i <= n; i++) printf("%d ", a[i]);
}