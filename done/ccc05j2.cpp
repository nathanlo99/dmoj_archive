#include <bits/stdc++.h>

using namespace std;
bool RSA(int c) {
    int count;
    count = 0;
    for (int j = 2; j < c; j++) {
        if (c % j == 0) {
            count++;
        }
    }
 if (count == 2) {
     return true;
 }
 return false;
}

int main() {
    int count;
    int a;
    int b;
    cin >> a;
    cin >> b;
    count = 0;
    for (int i = a; i <= b; i++) {
        if (RSA(i)) { 
            count++;
        }
    }
    cout <<"The number of RSA numbers between " << a << " and " << b << " is " << count <<endl;
    return 0;
}