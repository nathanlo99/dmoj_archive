#include <iostream>

#include <string>
#include <map>

int n, a;
std::string names[10005];
int freq[10005];
int maxn, maxnum;
std::map<std::string, int> lookup;
std::map<int, int> lookup_num;

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        std::cin >> names[i] >> a;
        lookup[names[i]] = i;
        lookup_num[a] = i;
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a);
        int r = lookup_num[a];
        freq[r]++;
        if (freq[r] > maxn || (freq[r] == maxn && a < maxnum)) {
            maxn = freq[r];
            maxnum = a;
        }
    }
    printf("%s\n", names[lookup_num[maxnum]].c_str());
}