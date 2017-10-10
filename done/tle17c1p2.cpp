#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>

std::map<std::string, int> values;
std::vector<std::pair<int, int> > things;

std::string s;
int f, e, n;

int main() {
    std::cin >> f;
    for (int i = 0; i < f; i++) {
        std::cin >> s >> e;
        values[s] = e;
    }
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> s >> e;
        things.push_back(std::make_pair(e, values[s]));
    }

    std::sort(things.begin(), things.end());

    for (std::pair<int, int> t: things) {
        // printf("%d %d\n", t.first, t.second);
    }

    int energy = 0, last_dist = 0, dist, value, ans = 0;
    for (std::pair<int, int> t: things) {
        std::tie(dist, value) = t;
        energy -= (dist - last_dist);
        if (dist != last_dist && energy < 0) break;
        energy += value;
        ans++;
        last_dist = dist;
        // printf("After eating: E: %d, L: %d\n", energy, last_dist);
    }

    printf("%d\n", ans);
}