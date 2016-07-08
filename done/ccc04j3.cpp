#include <iostream>
#include <string>

using namespace std;

int main(){
    int N, M;
    cin >> N >> M;
    string n[5], a[5];
    for(int i = 0; i < N; i++){
        cin >> n[i];
    }
    for(int i = 0; i < M; i++){
        cin >> a[i];
        for(int j = 0; j < N; j++){
            cout << n[j] << " as " << a[i] << endl;
        }
    }
}
