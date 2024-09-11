#include <bits/stdc++.h>
using namespace std;



int main(void) {
    int n, m;
    cin >> m >> n;
    int board[n][m];
    int dist[n][m];
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};
    
    queue<pair<int, int>> Q;
    for (int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            int s;
            cin >> s;
            board[i][j] = s;
            if (s == 1){
                Q.push({i, j});
                dist[i][j] = 1;
            }
            else{
                dist[i][j] = 0;
            }
        }
    }


    while(!Q.empty()){
        pair<int, int> cur = Q.front();
        int curDist = dist[cur.first][cur.second];
        Q.pop();

        for(int k = 0; k < 4; k++){
            int curDx = cur.first + dx[k];
            int curDy = cur.second + dy[k];

            if (curDx < 0 || curDx >= n || curDy < 0 || curDy >= m) continue;
            if (board[curDx][curDy] == 0) {
                Q.push({curDx, curDy});
                board[curDx][curDy] = 1;
                dist[curDx][curDy] = curDist + 1;
            }
        }
    }



    int maxNum = 1;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if (board[i][j] == 0) {
                cout << -1;
                return 0;
            }
           if (maxNum < dist[i][j]) maxNum = dist[i][j];
        }
    }
    cout << maxNum-1;
}