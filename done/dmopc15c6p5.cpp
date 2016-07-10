#include <iostream>
#include <deque>
using namespace std;

int N, K, a[3000002];
deque<int> minQ, maxQ;
long long ans;

int main() {
    scanf("%d %d", &N, &K);
    for (int i = 1; i <= N; i++) {
        scanf("%d", &a[i]);
    }

    for (int l = 1, r = 1; r <= N; r++) {
        while(!minQ.empty() && a[r] < minQ.back()) minQ.pop_back();
        while(!maxQ.empty() && a[r] > maxQ.back()) maxQ.pop_back();
        minQ.push_back(a[r]);
        maxQ.push_back(a[r]);
        while (maxQ.front() - minQ.front() > K) {
            if(maxQ.front() == a[l]) maxQ.pop_front();
            if(minQ.front() == a[l]) minQ.pop_front();
            l++;
        }
        ans += r - l + 1;
    }
    printf("%lld\n", ans);
}
