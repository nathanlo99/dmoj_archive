#include <cstdio>
#include <vector>

using namespace std;
int N, M, A, B, has_in[100000], has_out[100000];
long long times[100000], path[100000];
vector<int> adj[100000];

int main() {
  scanf("%d %d", &N, &M);
  for (int i = 0; i < M; i++) {
    scanf("%d %d", &A, &B);
    adj[A - 1].push_back(B - 1);
    has_in[B - 1] = 1;
    has_out[A - 1] = 1;
  }

  for (int i = 0; i < N; i++) {
    if (!has_in[i]) {
      times[i] = 0;
      path[i] = 1;
    }

    for (int j = 0; j < adj[i].size(); j++) {
      const int dest = adj[i][j];
      times[dest] = (times[dest] + times[i] + path[i]) % 1000000007L;
      path[dest] = (path[dest] + path[i]) % 1000000007L;
    }
  }

  long long ans = 0;
  for (int i = 0; i < N; i++) {
    if (!has_out[i])
      ans = (ans + times[i]) % 1000000007L;
  }
  printf("%lld\n", ans);
  return 0;
}