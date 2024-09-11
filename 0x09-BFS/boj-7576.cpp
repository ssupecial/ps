#include <bits/stdc++.h>
#define X first 
#define Y second
using namespace std;


int main(void){
    int n, m;
    cin >> m >> n;
    int board[n][m];
    int start = 1;
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};
    queue<pair<int, int>> Q;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            int value;
            cin >> value;
            board[i][j] = value;
            if (value == 1) 
                Q.push({i, j});
        }
    }

    while(!Q.empty()){
        pair<int, int> cur = Q.front();
        Q.pop();

        int num = board[cur.X][cur.Y];

        for (int i = 0; i < 4; i++){
            int nx = cur.X + dx[i];
            int ny = cur.Y + dy[i];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(board[nx][ny] == 0){
                board[nx][ny] = num + 1;
                Q.push({nx, ny});
            }

        }

    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if(board[i][j] == 0){
                cout << -1;
                return 0;
            }
            if(board[i][j] >  start)
                start = board[i][j];
        }
    }

    cout << start-1;


}