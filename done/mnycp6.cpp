#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <iostream>

using namespace std;

long long n = 1, c, bit[10005];
map<string, int> idx, mass_;
string op, r, x, y;

int mass(string s) {
    if (mass_.count(s) == 0) {
        int res = 0;
        for (char c : s) res += (c - 'a') + 1;
        mass_[s] = res;
    }
    return mass_[s];
}

void update(int idx, int amt) {
    for (int a = idx; a <= 10005; a += a & -a) bit[a] += amt;
}

long long query(int idx) {
    long long res = 0;
    for (int a = idx; a > 0; a -= a & -a) res += bit[a];
    return res;
}

int main() {
    scanf("%d", &c);
    for (int i = 0; i < c; i++) {
        cin >> op;
        if (op == "A") {
            cin >> r;
            if (idx.count(r) != 0) {
                cout << "Can't add " << r << endl;
            } else {
                update(n, mass(r));
                idx[r] = n++;
            }
        } else if (op == "S") {
            cin >> x >> y;
            int massX = mass(x), massY = mass(y);
            int idxX = idx[x], idxY = idx[y];
            update(idxX, massY - massX);
            update(idxY, massX - massY);
            idx[y] = idxX; idx[x] = idxY;
        } else if (op == "M") {
            cin >> x >> y;
            int idxX = idx[x], idxY = idx[y];
            if (idxY < idxX) swap(idxX, idxY);
            printf("%lld\n", query(idxY) - query(idxX - 1));
        } else if (op == "R") {
            cin >> x >> y;
            int massDiff = mass(y) - mass(x);
            int idxX = idx[x];
            update(idxX, massDiff);
            idx.erase(x);
            idx[y] = idxX;
        } else if (op == "N") {
            printf("%d\n", n - 1);
        }
    }
}