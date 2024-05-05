#include <bits/stdc++.h>
using namespace std;

int main(void){
    int board[100][100];
    int dist[100][100];
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n ; i++){
        string s;
        cin >> s;
        for (int k = 0; k < m; k++){
            board[i][k] = s[k] - '0';
            dist[i][k] = -1;
        }
    }

    queue<pair<int, int>> Q;
    dist[0][0] = 0;
    Q.push({0,0});

    while(!Q.empty()){
        pair<int, int> cur = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++){
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (dist[nx][ny] > -1) continue;
            if (board[nx][ny] == 0) continue;

            dist[nx][ny] = dist[cur.first][cur.second] + 1;
            Q.push({nx, ny});
        }
        
    }

    cout << dist[n-1][m-1] + 1;




}