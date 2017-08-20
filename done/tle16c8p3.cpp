#include <cstdio>
#include <vector>
#include <algorithm>

#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;

long long dp[128], t, n;
std::vector<long long> psa;

int main() {
    dp[0] = dp[1] = 0;
    dp[2] = dp[3] = 1;
    psa.push_back(0);
    psa.push_back(0);
    psa.push_back(1);
    psa.push_back(2);
    for (int i = 4; i < 128; i++) {
        dp[i] = dp[i - 2] + dp[i - 3];
        psa.push_back(psa.back() + dp[i]);
    }
    
    scan(t);
    while (t--) {
        scan(n);
        int d = std::lower_bound(psa.begin(), psa.end(), n) - psa.begin();
        n -= psa[d - 1] + 1;
        while (d > 0) {
            if (d == 2) { puts("69\n"); break; }
            if (d == 3) { puts("420\n"); break; }
            if (n < dp[d - 3]) {
                printf("420");
                d -= 3;
            } else {
                printf("69");
                n -= dp[d - 3];
                d -= 2;
            }
        }
    }
}