#include <bits/stdc++.h>
using namespace std;


int main(void){
    int board[100][100];
    int visited[100][100];
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};
    int dist[100][100];
    int n, m;
    cin >> n >> m;
    

    for (int i = 0; i < n; i++){
        string s;
        cin >> s;
        for (int j = 0; j < m; j++){
            board[i][j] = s[j] - '0';
            visited[i][j] = 0;
            dist[i][j] = 0;
        }
        
    }

    queue<pair<int, int>> Q;
    Q.push({0,0});
    visited[0][0] = 1;
    dist[0][0] = 1;

    while(!Q.empty()){
        pair<int, int> cur = Q.front();
        int curDist = dist[cur.first][cur.second];
        Q.pop();

        for (int k = 0; k < 4; k ++){
            int curDx = cur.first + dx[k];
            int curDy = cur.second + dy[k];

            if (curDx < 0 || curDx >= n || curDy < 0 || curDy >= m) continue;
            if (board[curDx][curDy] == 0 || visited[curDx][curDy] == 1) continue;

            visited[curDx][curDy] = 1;
            dist[curDx][curDy] = curDist + 1;
            Q.push({curDx, curDy});

        }
    }

    cout << dist[n-1][m-1];

}