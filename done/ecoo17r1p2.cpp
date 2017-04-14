#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

struct Ch{
    string name = "";
    int P = 0,F = 0,G = 0;
    bool operator<(const Ch &o) const{
        if (P+F+G == o.P+o.F+o.G){
            if (G == o.G){
                if (F == o.F){
                    return P < o.P;
                }
                return F < o.F;
            }
            return G < o.G;
        }
        return P+F+G < o.P + o.F + o.G;
    }
    bool operator!=(const Ch &o) const{
        return P != o.P || F != o.F || G != o.G;
    }
};

int T = 10;
int N;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    while(T--){
        vector<Ch> vect;
        vect.clear();
        cin >> N;
        string buffer = "";
        cin >> buffer;
        for (int i = 0; i < N; i++){
            Ch ch;
            ch.name = buffer;
            while(cin >> buffer && buffer == "J"){
                int p,f,g;
                cin >> p >> f >> g;
                ch.P += p, ch.F += f, ch.G += g;
            }
            vect.push_back(ch);
        }
        sort(vect.begin(),vect.end());
        cout << vect.back().name;
        for (int i = (int)vect.size()-2; i >= 0; i--){
            if (vect[i] != vect.back()) break;
            cout << ", " << vect[i].name;
        }
        cout << "\n";
    }
    return 0;
}