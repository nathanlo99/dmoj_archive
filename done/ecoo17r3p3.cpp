#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
#define sq(x) (x)*(x)

int N;
int X[105],Y[105];

double getBestDist(vector<int> v, int ar[]){
    if (v.empty()) return 0;
    //(x-ar[i])^2
    //x^2 - 2ar[i] + ar[i]^2
    double a = 0, b = 0, c = 0;
    for (int i : v){
        a++, b -= 2*ar[i], c += sq(ar[i]);
    }
    double bestX = -b/(2*a);
    //return bestX;
    return a*sq(bestX) + b*bestX + c;
}

double getAns(vector<int> v){
    return getBestDist(v,X)+getBestDist(v,Y);
}

void do_case() {
    scanf("%d",&N);
    for (int i = 1; i <= N; i++){
        scanf("%d%d",&X[i],&Y[i]);
    }
    if (N == 1){
        printf("0\n");
        return;
    }
    double ans = 2e9;
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            if (i==j) continue;
            double A,B,C;
            A = (Y[i]-Y[j]), B = (X[j]-X[i]), C = X[i]*Y[j]-Y[i]*X[j];
            vector<int> s1, s2;
            for (int k = 1; k <= N; k++){
                if (A*X[k] + B*Y[k] + C > 0) s1.push_back(k);
                else if (A*X[k] + B*Y[k] + C == 0){
                    if (B == 0){
                        if (Y[k] >= Y[i]) s1.push_back(k);
                        else s2.push_back(k);
                    }else{
                        if (X[k] >= X[i]) s1.push_back(k);
                        else s2.push_back(k);
                    }
                }
                else s2.push_back(k);
            }
            //printf("s1: "); for (int n : s1) printf("%d ",n);
            //printf("\ns2: "); for (int n : s2) printf("%d ",n);
            //printf("\n");
            //printf("try: %lf %lf\n",getAns(s1),getAns(s2));
            ans = min(ans,getAns(s1)+getAns(s2));
        }
    }
    // printf("%lf\n", ans);
    printf("%d\n",(int)round(ans));
}

int T = 10;
int main() {
    while (T--) do_case();
}