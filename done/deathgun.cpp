#include <cstdio>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;
int M, tot, in[900];
unordered_map<string, int> dict;
string name[900], A, B;
vector<int> adj[900];

int main() {
  scanf("%d", &M);
  for (int i = 0; i < M; i++) {
    cin >> A >> B;
    if (dict.count(A) == 0) {
      dict[A] = tot;
      name[tot++] = A;
    }
    if (dict.count(B) == 0) {
      dict[B] = tot;
      name[tot++] = B;
    }
    adj[dict[B]].push_back(dict[A]);
    in[dict[A]]++;
  }

  while (true) {
    bool flag = false;
    for (int i = 0; i < tot; i++) {
      if (in[i] == 0) {
        cout << name[i] << endl;
        in[i]--;
        flag = true;
        for (auto v : adj[i])
          in[v]--;
      }
      if (flag)
        break;
    }
    if (!flag)
      break;
  }
  return 0;
}