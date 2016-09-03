#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

string repeat(char c, int n){
    string r = "";
    for(int i = 0; i < n; i++){
        r += c;
    }
    return r;
}

int main(){
    int N;
    cin >> N;
    int d = N/2, b = 1;
    cout << repeat('*', N) << endl;
    for(int i = 1; i < N / 2; i++){
        cout << repeat('*', d) << repeat(' ', b) << repeat('*', d) << endl;
        d -= 1;
        b += 2;
    }
    d = 1;
    b = N - 2;
    for(int i = 1; i <= N/2; i++){
        cout << repeat('*', d) << repeat(' ', b) << repeat('*', d) << endl;
        d += 1;
        b -= 2;
    }
    cout << repeat('*', N) << endl;
	return 0;
}