#include <bits/stdc++.h>
using namespace std;

vector<int> adj[100001];
int priority[100001];
int correct_path[100001];
int given_path[100001];
int visited[100001];
int num = 1;

bool compare_priority(int a, int b){
    return priority[a] < priority[b];
}

void DFS(int x){
    correct_path[num++] = x;
    visited[x] = 1;

    for(int i = 0; i < adj[x].size(); i++){
        int cur = adj[x][i];
        if(visited[cur] == 0) {
            DFS(cur);
        }
    }
}


int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for(int i = 1; i < n; i++){
        int value1, value2;
        cin >> value1 >> value2;
        adj[value1].push_back(value2);
        adj[value2].push_back(value1);
    }

    for(int i = 1; i <= n; i++){
        int value;
        cin >> value;
        priority[value] = i;
        given_path[i] = value;
    }

    // 각 인접 배열 정렬
    // for (int i = 1; i <= n; i++){
    //     sort(adj[i].begin(), adj[i].end(), compare_priority);
    // }
    for (int i = 1; i <= n; i++) {
        sort(adj[i].begin(), adj[i].end(), compare_priority);
    }

    DFS(1);

    for (int i = 1; i <= n; i++){
        if (correct_path[i] != given_path[i]) {
            cout << 0;
            return 0;
        }
    }

    cout << 1;
    return 0;



}