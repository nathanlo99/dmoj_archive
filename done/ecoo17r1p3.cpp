//
//  main.cpp
//  p3
//
//  Created by Nathan Lo on 2017-03-31.
//  Copyright © 2017 Nathan Lo. All rights reserved.
//

#include <iostream>
#include <stdio.h>
using namespace std;

int n;

double moun[100005];

double slop,td;
int bestidx,bestcnt,cnt;

void docase()
{
    cin >> n;
    for (int i=0; i<n; i++) cin >> moun[i];
    bestidx=0;
    bestcnt=0;
    for (int i=0; i<n; i++) {
        slop=-1000000;
        cnt=0;
        for (int j=i+1; j<n; j++) {
            td=(moun[j]-moun[i])/(j-i);
            if (slop+1e-14<td) {
                slop=td;
                cnt++;
            }
        }
        slop=-1000000;
        for (int j=i-1; j>=0; j--) {
            td=-(moun[j]-moun[i])/(j-i);
            if (slop+1e-14<td) {
                slop=td;
                cnt++;
            }
        }
        //printf("test %d %d\n",i,cnt);
        // best
        if (bestcnt<cnt) {
            bestcnt=cnt;
            bestidx=i;
        }
    }
    cout << bestidx+1 << endl;
    
}

int main(int argc, const char * argv[]) {
    for (int i=0; i<10; i++) docase();
}