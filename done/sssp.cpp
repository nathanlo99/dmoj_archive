#include <cmath>
#include <cstdio>

#include <vector>

using namespace std;

int N, M, A, B, C, vis[1001], dist[1001];
vector<pair<int, int>> graph[1001];

void dijkstra_list() {
  for (int i = 1; i <= N; i++) {
    dist[i] = 0x3f3f3f3f;
  }
  dist[1] = 0;

  for (int num = 1; num <= N; num++) {
    int minNode = -1;
    int minDist = 0x3f3f3f3f;

    for (int i = 1; i <= N; i++) {
      if (!vis[i] && dist[i] < minDist) {
        minDist = dist[i];
        minNode = i;
      }
    }

    if (minNode == -1)
      return;

    vis[minNode] = 1;

    for (int i = 0; i < graph[minNode].size(); i++) {
      int dest = graph[minNode][i].first;
      if (vis[dest])
        continue;
      int weight = graph[minNode][i].second;
      if (dist[minNode] + weight < dist[dest])
        dist[dest] = dist[minNode] + weight;
    }
  }
}

int main() {
  scanf("%d %d", &N, &M);
  for (int i = 0; i < M; i++) {
    scanf("%d %d %d", &A, &B, &C);
    graph[A].push_back(make_pair(B, C));
    graph[B].push_back(make_pair(A, C));
  }
  dijkstra_list();
  for (int i = 1; i <= N; i++) {
    if (dist[i] == 0x3f3f3f3f)
      printf("-1\n");
    else
      printf("%d\n", dist[i]);
  }
  return 0;
}