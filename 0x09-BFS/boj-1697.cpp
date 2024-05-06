#include <bits/stdc++.h>
using namespace std;

int visited[1000002];

int main(void){
    int n, m;
    cin >> n >> m;
    int result;

    queue<pair<int, int>> Q;

    Q.push({n, 0});
    visited[n] = 1;

    while (!Q.empty()){
        pair<int, int> cur = Q.front();
        Q.pop();
        if (cur.first == m){
            result = cur.second;
            break;
        }


        if (!(cur.first-1 < 0 || visited[cur.first-1] == 1)) { // X-1
            Q.push({cur.first-1, cur.second+1});
            visited[cur.first-1] = 1;
        }
        if (!(cur.first+1 > 1000000 || visited[cur.first+1] == 1)) { // X+1
            Q.push({cur.first+1, cur.second+1});
            visited[cur.first+1] = 1;
        }
        if (!(cur.first * 2 > 1000000)) {
            Q.push({cur.first*2, cur.second+1});
            visited[cur.first*2] = 1;
        }
    }

    cout << result;

}