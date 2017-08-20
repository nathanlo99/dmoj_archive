#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstring>
#define INF 0x3f3f3f3f

using namespace std;

struct Period{
    int p;
    vector<int> stu;
} data[1005];

bool cmp(Period &p1, Period &p2){
    return p1.p < p2.p;
}

int N;
int nerd, girl, dist[1005];
vector<int> graph[1005], st, goal;
bool isGoal[1005];
map<int, vector<int> > students;
map<int, set<int> > periods;

int main(){
    scanf("%d",&N);
    scanf("%d %d",&nerd, &girl);
    for (int i = 0, s, stu; i < N; i++){
        scanf("%d%d", &data[i].p, &s);
        set<int> taken;
        while(s--){
            scanf("%d", &stu);
            data[i].stu.push_back(stu);
            periods[stu].insert(data[i].p);
        }
    }
    sort(data, data+N, cmp);
    for (int i = 0; i < N; i++) {
        for (int stu : data[i].stu) {
            if (stu == nerd) st.push_back(i);
            else if (stu == girl) goal.push_back(i);
            for (int cl : students[stu])
                graph[cl].push_back(i);
            students[stu].push_back(i);
        }
    }
    
    memset(dist,0x3f,sizeof(dist));
    queue<int> q;
    for (int cl : st){
        q.push(cl);
        dist[cl] = 1;
    }
    
    while(!q.empty()){
        const int cur = q.front(); q.pop();
        for (int cl : graph[cur]){
            if (dist[cl] == INF){
                dist[cl] = dist[cur] + 1;
                q.push(cl);
            }
        }
    }
    
    int ans1 = INF, ans2 = INF;
    for (int cl : goal){
        if (dist[cl] < ans1){
            ans1 = dist[cl];
            ans2 = data[cl].p;
        } else if (dist[cl] == ans1) {
            ans2 = min(ans2, data[cl].p);
        }
    }
    if (ans1 == INF) printf("delivery failure\n");
    else printf("%d\n%d\n", ans1, ans2);
}