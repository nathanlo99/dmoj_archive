#include <bits/stdc++.h>

int n;
long long m,k;
long long arr[100005];

long long lo,hi,mid;

void do_case() {
    scanf("%d",&n);
    scanf("%lld%lld",&m,&k);
    for (int i=0; i<n; i++) scanf("%lld",&arr[i]);
    lo=0xafafafafafafafaf;
    hi=0x3f3f3f3f;
    while (lo<=hi) {
        mid=(lo+hi)/2;      // make restaurant rating <= mid
        long long downs=0;
        long long exacts=0;
        for (int i=0; i<n; i++) {
            if (arr[i]>=mid) {
                if ((arr[i]-mid)%m==0) {
                    exacts++;
                    downs+=(arr[i]-mid)/m;
                }
                else {
                    downs+=(arr[i]-mid)/m+1;
                }
            }
            if (downs>=k) break;
        }
        if (downs>=k) {
            lo=mid+1;
        } else if (downs+exacts<k) {
            hi=mid-1;
        }
        else {
            int idx=k-downs;
            for (int i=0; i<n; i++) {
                if (arr[i]>=mid && (arr[i]-mid)%m==0) {
                    idx--;
                    if (idx==0) {
                        printf("%d\n",i+1);
                        return;
                    }
                }
            }
        }
    }
    // printf("fail\n");
}

int T = 10;

int main() {
    while (T--) do_case();
}