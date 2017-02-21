#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>


int t, n;
std::string s;
std::map<std::string, int> order;
std::vector<std::pair<int, int> > problems;

int main() {
    scanf("%d ", &t);
    for (int i = 0; i < t; i++) {
        std::getline(std::cin, s);
        order[s] = i;
    }
    scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
        std::getline(std::cin, s);
        problems.push_back(std::make_pair(order[s], i));
    }
    std::sort(problems.begin(), problems.end());

    for (auto p : problems) {
        printf("%d\n", p.second + 1);
    }
}