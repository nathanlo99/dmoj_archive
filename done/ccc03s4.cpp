#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

int n;
std::string s;
std::vector<std::string> suffix;

int lcp(std::string a, std::string b) {
    const int l = std::min(a.length(), b.length());
    for (int i = 0; i < l; i++) {
        if (a[i] != b[i]) {
            return i;
        }
    }
    return l;
}

int main() {
    scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
        suffix = std::vector<std::string>();
        std::getline(std::cin, s);
        for (int i = 0; i < s.length(); i++) suffix.push_back(s.substr(i));
        std::sort(suffix.begin(), suffix.end());
        int ans = suffix[0].length();
        for (int i = 1; i < suffix.size(); i++) {
            int l = lcp(suffix[i], suffix[i - 1]);
            ans += suffix[i].length() - l;
        }
        printf("%d\n", ans + 1);
    }
}