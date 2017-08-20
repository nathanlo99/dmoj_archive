// convert to c++ code
#include <stdio.h>
#include <string.h>

#define getchar getchar_unlocked
#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;

#define mod 1000000007

int n,det;
long long mult;
int m[500][500];
int t[500];
bool nonzero=true;

// function could be better
inline void modinverse(int i)
{
    mult=1;
    while (i!=1) {
        int t=mod/i+1;
        mult=(mult*t)%mod;
        i=(i*t)%mod;
    }
}

int main()
{
    // inputs
    // note that det is a temporary variable
    scan(n);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            scan(det);
            m[i][j]=(det+mod)%mod;
        }
    }
    // calculations
    det=1;
    for (int i=0; i<n-1; i++) {
        if (m[i][i]==0) {
            nonzero=false;
            for (int j=i+1; j<n; j++) {
                if (m[j][i]) {
                    nonzero=true;
                    memcpy(t,m[i],n*4);
                    memcpy(m[i],m[j],n*4);
                    memcpy(m[j],t,n*4);
                    if ((j+i)&1) det=mod-det;
                    break;
                }
            }
        }
        if (!nonzero) break;
        if (m[i][i]!=1) {
            modinverse(m[i][i]);
            m[i][i]=1;
            for (int j=i+1; j<n; j++) {
                m[i][j]=(m[i][j]*mult)%mod;
            }
            det=(det*mult)%mod;
        }
        for (int j=i+1; j<n; j++) {
            if (m[j][i]) {
                mult=mod-m[j][i];
                m[j][i]=0;
                for (int k=i+1; k<n; k++) {
                    m[j][k]=(m[j][k]+mult*m[i][k])%mod;
                }
            }
        }
    }
    if (m[n-1][n-1]) {
        modinverse(m[n-1][n-1]);
        det=(det*mult)%mod;
    }
    else nonzero=false;

    if (nonzero) {
        modinverse(det);
        printf("%lld",mult);
    }
    else putchar('0');
}