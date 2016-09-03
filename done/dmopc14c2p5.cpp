#include <bits/stdc++.h>
using namespace std;

int a, b, x, y;
vector<int> graph[1000000];
double prob[1000000];

int main() {
  scanf("%d %d", &a, &b);

  for (int i = 0; i < b; i++) {
    scanf("%d %d", &x, &y);
    graph[x - 1].push_back(y - 1);
  }

  prob[0] = 1;
  for (int i = 0; i < a; i++) {
    const double temp = prob[i] / graph[i].size();
    for (int j = 0; j < graph[i].size(); j++) {
      prob[graph[i][j]] += temp;
    }
    if (graph[i].size() == 0) {
      printf("%.12lf\n", prob[i]);
    }
  }
}