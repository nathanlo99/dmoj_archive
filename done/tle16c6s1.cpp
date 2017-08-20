#include <cstdio>
#include <iostream>
#include <algorithm>
#include <unordered_map>

int t, n;
std::string s;
std::unordered_map<std::string, int> order;
std::pair<int, int> problems[100005];

int main() {
    std::cin.tie(0);
    std::cin.sync_with_stdio(0);
    std::cin >> t;
    for (int i = 0; i < t; i++) {
        std::cin >> s;
        order[s] = i;
    }
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        problems[i].first = order[s];
        problems[i].second = i;
    }
    std::sort(problems, problems + n);
    for (int i = 0; i < n; i++) printf("%d\n", problems[i].second + 1);
}