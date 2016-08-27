#include <iostream>
#include <cstdio>
#include <unordered_set>

#define magic isThisWilliamsSolution

using namespace std;

int N,A,B;
unordered_set<int> seq;

int main(){
    seq.insert(1);
    seq.insert(2);
    seq.insert(6);
    seq.insert(20);
    seq.insert(70);
    seq.insert(252);
    seq.insert(924);
    seq.insert(3432);
    seq.insert(12870);
    seq.insert(48620);
    seq.insert(184756);
    seq.insert(705432);
    scanf("%d",&N);
    for (int i = 1; i <= N; i++){
        scanf("%d%d",&A,&B);
        if (seq.count(i)) printf("%d\n",A-B);
        else printf("%d\n",A+B);
    }
    return 0;
}